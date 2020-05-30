"""kdjaflkdajs

Revision ID: 19fabfe05555
Revises: 9c04856cdbbe
Create Date: 2020-05-19 19:54:48.675340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19fabfe05555'
down_revision = '9c04856cdbbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('extras',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('price', sa.DECIMAL(precision=2, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('subs2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('price', sa.DECIMAL(precision=2, scale=2), nullable=True),
    sa.Column('price2', sa.DECIMAL(precision=2, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subs2')
    op.drop_table('extras')
    # ### end Alembic commands ###
