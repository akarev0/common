"""empty message

Revision ID: cd6a50d211cb
Revises: a65ea854841b
Create Date: 2020-02-09 19:20:58.893139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd6a50d211cb'
down_revision = 'a65ea854841b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('libraries',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('libraries')
    # ### end Alembic commands ###
