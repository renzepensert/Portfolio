"""pr

Revision ID: 9c04856cdbbe
Revises: 424fdff8f143
Create Date: 2020-05-19 16:48:40.955460

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9c04856cdbbe'
down_revision = '424fdff8f143'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rpizza', 'price11')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rpizza', sa.Column('price11', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
