"""empty message

Revision ID: 003cef153559
Revises: 19fa41715faa
Create Date: 2020-01-05 13:24:44.229557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003cef153559'
down_revision = '19fa41715faa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('library', sa.Column('book_title', sa.String(), nullable=False))
    op.create_foreign_key(None, 'library', 'books', ['book_title'], ['book_title'])
    op.drop_column('library', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('library', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'library', type_='foreignkey')
    op.drop_column('library', 'book_title')
    # ### end Alembic commands ###
