"""update AppConfiguration

Revision ID: 198c383101dd
Revises: 59f615b01c3e
Create Date: 2019-09-03 19:49:18.530009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '198c383101dd'
down_revision = '59f615b01c3e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appconfig', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gluu_archive', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('latest_version', sa.String(length=10), nullable=True))
        batch_op.add_column(sa.Column('offline', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appconfig', schema=None) as batch_op:
        batch_op.drop_column('offline')
        batch_op.drop_column('latest_version')
        batch_op.drop_column('gluu_archive')

    # ### end Alembic commands ###
