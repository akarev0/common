"""empty message

Revision ID: e6bb8b722679
Revises: 003cef153559
Create Date: 2020-01-05 13:32:58.827339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6bb8b722679'
down_revision = '003cef153559'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('books_library_id_fkey', 'books', type_='foreignkey')
    op.drop_column('books', 'library_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('library_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('books_library_id_fkey', 'books', 'library', ['library_id'], ['id'])
    # ### end Alembic commands ###
