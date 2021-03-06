"""add billing add and delivery add fileds into user model

Revision ID: b55cf83dcf40
Revises: 8c3eb906dd2e
Create Date: 2020-03-03 16:49:50.635048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b55cf83dcf40'
down_revision = '8c3eb906dd2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('billing_address', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('delivery_address', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'delivery_address')
    op.drop_column('users', 'billing_address')
    # ### end Alembic commands ###
