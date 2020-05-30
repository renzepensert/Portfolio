"""password weg

Revision ID: 90d948e30dce
Revises: f55d793017c8
Create Date: 2020-05-10 15:51:22.853196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90d948e30dce'
down_revision = 'f55d793017c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
