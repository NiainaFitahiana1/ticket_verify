from quart import Blueprint, request, jsonify, g
from .schemas import ProductCreateSchema, ProductOutSchema
from .models import Product
from .db import get_session
from .auth import auth_required
from sqlalchemy.future import select


products_bp = Blueprint('products', __name__)




@products_bp.route('/', methods=['GET'])
async def list_products():
async for session in get_session():
q = await session.execute(select(Product).order_by(Product.id))
items = q.scalars().all()
schema = ProductOutSchema(many=True)
return jsonify(schema.dump(items))




@products_bp.route('/', methods=['POST'])
@auth_required
async def create_product():
data = await request.get_json()
schema = ProductCreateSchema()
errors = schema.validate(data)
if errors:
return jsonify({'errors': errors}), 400


async for session in get_session():
p = Product(
name=data['name'],
description=data.get('description'),
price=float(data['price']),
in_stock=bool(data.get('in_stock', True)),
)
session.add(p)
await session.commit()
await session.refresh(p)
out = ProductOutSchema().dump(p)
return jsonify(out), 201




@products_bp.route('/<int:product_id>', methods=['GET'])
async def get_product(product_id):
async for session in get_session():
q = await session.execute(select(Product).filter_by(id=product_id))
p = q.scalars().first()
if not p:
return jsonify({'message': 'not found'}), 404
return jsonify(ProductOutSchema().dump(p))




@products_bp.route('/<int:product_id>', methods=['PUT'])
@auth_required
async def update_product(product_id):
data = await request.get_json()
schema = Prod