"""empty message

Revision ID: 45d3db3fb40e
Revises: 234e36d77bd4
Create Date: 2022-06-21 16:02:39.991349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45d3db3fb40e'
down_revision = '234e36d77bd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('types', sa.String(length=255), nullable=True),
    sa.Column('abilities', sa.String(length=255), nullable=True),
    sa.Column('moves', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('hp', sa.Integer(), nullable=True),
    sa.Column('defense', sa.Integer(), nullable=True),
    sa.Column('att', sa.Integer(), nullable=True),
    sa.Column('speed', sa.Integer(), nullable=True),
    sa.Column('sprite', sa.String(length=255), nullable=True),
    sa.Column('shiny_sprite', sa.String(length=255), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemon')
    # ### end Alembic commands ###
