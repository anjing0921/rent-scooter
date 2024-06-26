"""adds Customer Rental one to many 

Revision ID: 4148c22968c3
Revises: dc977e39e61f
Create Date: 2024-04-01 14:42:36.111040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4148c22968c3'
down_revision = 'dc977e39e61f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rental', schema=None) as batch_op:
        batch_op.add_column(sa.Column('customer_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'customer', ['customer_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rental', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('customer_id')

    # ### end Alembic commands ###
