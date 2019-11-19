"""empty message

Revision ID: 05a8515a9f09
Revises: e2fc6da27338
Create Date: 2019-11-19 07:03:49.247878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05a8515a9f09'
down_revision = 'e2fc6da27338'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('staff_salary_key', 'staff', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('staff_salary_key', 'staff', ['salary'])
    # ### end Alembic commands ###