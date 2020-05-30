"""pizzaanders

Revision ID: 357d86bdb7f1
Revises: 91ca36fd9b34
Create Date: 2020-05-19 15:12:47.257156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '357d86bdb7f1'
down_revision = '91ca36fd9b34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rpizza', sa.Column('price3', sa.Float(precision=5), nullable=True))
    op.add_column('rpizza', sa.Column('price4', sa.Float(precision=5), nullable=True))
    op.add_column('rpizza', sa.Column('price5', sa.Float(precision=5), nullable=True))
    op.add_column('rpizza', sa.Column('price6', sa.Float(precision=5), nullable=True))
    op.add_column('rpizza', sa.Column('price7', sa.Float(precision=5), nullable=True))
    op.add_column('rpizza', sa.Column('price8', sa.Float(precision=5), nullable=True))
    op.add_column('spizza', sa.Column('price3', sa.Float(precision=5), nullable=True))
    op.add_column('spizza', sa.Column('price4', sa.Float(precision=5), nullable=True))
    op.add_column('spizza', sa.Column('price5', sa.Float(precision=5), nullable=True))
    op.add_column('spizza', sa.Column('price6', sa.Float(precision=5), nullable=True))
    op.add_column('spizza', sa.Column('price7', sa.Float(precision=5), nullable=True))
    op.add_column('spizza', sa.Column('price8', sa.Float(precision=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('spizza', 'price8')
    op.drop_column('spizza', 'price7')
    op.drop_column('spizza', 'price6')
    op.drop_column('spizza', 'price5')
    op.drop_column('spizza', 'price4')
    op.drop_column('spizza', 'price3')
    op.drop_column('rpizza', 'price8')
    op.drop_column('rpizza', 'price7')
    op.drop_column('rpizza', 'price6')
    op.drop_column('rpizza', 'price5')
    op.drop_column('rpizza', 'price4')
    op.drop_column('rpizza', 'price3')
    # ### end Alembic commands ###
