"""adminuser

Revision ID: 09a0e3b4cb7b
Revises: 0dc4fde863d7
Create Date: 2020-05-13 18:56:12.833269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09a0e3b4cb7b'
down_revision = '0dc4fde863d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('isadmin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'isadmin')
    # ### end Alembic commands ###
