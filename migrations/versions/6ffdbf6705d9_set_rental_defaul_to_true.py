"""set rental defaul to true

Revision ID: 6ffdbf6705d9
Revises: 77aa8c342ada
Create Date: 2024-04-01 17:09:25.953721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ffdbf6705d9'
down_revision = '77aa8c342ada'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rental', schema=None) as batch_op:
        batch_op.alter_column('is_returned',
               existing_type=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('customer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('scooter_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rental', schema=None) as batch_op:
        batch_op.alter_column('scooter_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('customer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('is_returned',
               existing_type=sa.BOOLEAN(),
               nullable=False)

    # ### end Alembic commands ###