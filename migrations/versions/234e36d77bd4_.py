"""empty message

Revision ID: 234e36d77bd4
Revises: 1e49a544bbf3
Create Date: 2022-06-21 15:29:39.637220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '234e36d77bd4'
down_revision = '1e49a544bbf3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('types', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemon')
    # ### end Alembic commands ###
