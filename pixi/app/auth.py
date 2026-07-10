from quart import Blueprint, request, jsonify, current_app, g
auth_bp = Blueprint('auth', __name__)




async def init_first_admin(app):
# helper to create an initial admin if none exists (optional)
async for session in get_session():
q = await session.execute(select(Admin))
first = q.scalars().first()
if not first:
admin = Admin(username='admin', password_hash=hash_password('admin123'))
session.add(admin)
await session.commit()




def auth_required(fn):
@wraps(fn)
async def wrapper(*args, **kwargs):
auth_header = (await request.headers).get('Authorization')
if not auth_header or not auth_header.startswith('Bearer '):
return jsonify({'message': 'Missing token'}), 401
token = auth_header.split(' ', 1)[1]
payload = decode_token(token)
if not payload:
return jsonify({'message': 'Invalid or expired token'}), 401
# optionally attach admin info
g.admin = payload.get('sub')
return await fn(*args, **kwargs)


return wrapper




@auth_bp.route('/register', methods=['POST'])
async def register():
data = await request.get_json()
schema = LoginSchema()
errors = schema.validate(data)
if errors:
return jsonify({'errors': errors}), 400


username = data['username']
password = data['password']


async for session in get_session():
q = await session.execute(select(Admin).filter_by(username=username))
exists = q.scalars().first()
if exists:
return jsonify({'message': 'username already exists'}), 400
admin = Admin(username=username, password_hash=hash_password(password))
session.add(admin)
await session.commit()
return jsonify({'message': 'admin created'}), 201




@auth_bp.route('/login', methods=['POST'])
async def login():
data = await request.get_json()
schema = LoginSchema()
errors = schema.validate(data)
if errors:
return jsonify({'errors': errors}), 400


username = data['username']
password = data['password']


async for session in get_session():
q = await session.execute(select(Admin).filter_by(username=username))
admin = q.scalars().first()
if not admin or not verify_password(password, admin.password_hash):
return jsonify({'message': 'invalid credentials'}), 401
token = create_access_token({'id': admin.id, 'username': admin.username})
return jsonify({'access_token': token, 'token_type': 'bearer'}), 200




@auth_bp.route('/me', methods=['GET'])
@auth_required
async def me():
# g.admin is the payload['sub']
return jsonify(g.admin)