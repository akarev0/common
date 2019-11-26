"""empty message

Revision ID: a1c6212088f5
Revises: eb27782f043d
Create Date: 2019-11-21 06:17:52.088949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1c6212088f5'
down_revision = 'eb27782f043d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tenants', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tenants', sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###