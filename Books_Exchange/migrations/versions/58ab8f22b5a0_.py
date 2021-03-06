"""empty message

Revision ID: 58ab8f22b5a0
Revises: 54785e70fc5b
Create Date: 2020-02-09 18:06:51.508001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58ab8f22b5a0'
down_revision = '54785e70fc5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('library',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('books', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.drop_constraint('books_user_id_fkey', 'books', type_='foreignkey')
    op.create_foreign_key(None, 'books', 'users', ['owner_id'], ['id'])
    op.drop_column('books', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.create_foreign_key('books_user_id_fkey', 'books', 'users', ['user_id'], ['id'])
    op.drop_column('books', 'owner_id')
    op.drop_table('library')
    # ### end Alembic commands ###
