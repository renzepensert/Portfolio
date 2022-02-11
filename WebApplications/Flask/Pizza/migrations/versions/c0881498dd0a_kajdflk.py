"""kajdflk

Revision ID: c0881498dd0a
Revises: 19fabfe05555
Create Date: 2020-05-19 20:00:55.997661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0881498dd0a'
down_revision = '19fabfe05555'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subs2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subs2',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=60), autoincrement=False, nullable=True),
    sa.Column('price', sa.NUMERIC(precision=2, scale=2), autoincrement=False, nullable=True),
    sa.Column('price2', sa.NUMERIC(precision=2, scale=2), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='subs2_pkey'),
    sa.UniqueConstraint('name', name='subs2_name_key')
    )
    # ### end Alembic commands ###