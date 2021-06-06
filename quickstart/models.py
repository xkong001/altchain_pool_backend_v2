# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AddressWhiteList(models.Model):
    uuid = models.CharField(primary_key=True, max_length=16)
    user_uuid = models.ForeignKey('User', models.DO_NOTHING, db_column='user_uuid')
    address = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    ext_data = models.CharField(max_length=100, blank=True, null=True)
    gmt_create = models.IntegerField(blank=True, null=True)
    gmt_update = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_white_list'


class BillStatus(models.Model):
    miner = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(primary_key=True, max_length=100)
    balance = models.FloatField(blank=True, null=True)
    init_balance = models.FloatField(blank=True, null=True)
    pendding_balance = models.FloatField(blank=True, null=True)
    total_paid = models.FloatField(blank=True, null=True)
    pay1day = models.FloatField(blank=True, null=True)
    pay1week = models.FloatField(blank=True, null=True)
    paid30days = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_status'


class Coin(models.Model):
    id = models.IntegerField(primary_key=True)
    currency = models.CharField(max_length=8)
    algorithm = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coin'


class CurrencyPoolStatus(models.Model):
    currency = models.CharField(primary_key=True, max_length=8)
    blocks = models.IntegerField(blank=True, null=True)
    hashrate = models.FloatField(blank=True, null=True)
    miners = models.IntegerField(blank=True, null=True)
    workers = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currency_pool_status'


class CurrencyStatus(models.Model):
    currency = models.CharField(primary_key=True, max_length=8)
    income = models.FloatField(blank=True, null=True)
    mean_income_24h = models.FloatField(blank=True, null=True)
    income_hashrate = models.IntegerField(blank=True, null=True)
    usd = models.FloatField(blank=True, null=True)
    cny = models.FloatField(blank=True, null=True)
    network_hashrate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currency_status'


class DefaultAccount(models.Model):
    user_uuid = models.OneToOneField('User', models.DO_NOTHING, db_column='user_uuid', primary_key=True)
    subuser_uuid = models.ForeignKey('Subuser', models.DO_NOTHING, db_column='subuser_uuid')

    class Meta:
        managed = False
        db_table = 'default_account'


class DefaultMiner(models.Model):
    user_uuid = models.OneToOneField('User', models.DO_NOTHING, db_column='user_uuid', primary_key=True)
    subuser_uuid = models.ForeignKey('Subuser', models.DO_NOTHING, db_column='subuser_uuid')
    currency = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_miner'


class EmailCode(models.Model):
    email = models.CharField(primary_key=True, max_length=100)
    code = models.CharField(max_length=8, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_code'


class FollowWallet(models.Model):
    user_uuid = models.ForeignKey('User', models.DO_NOTHING, db_column='user_uuid')
    wallet = models.CharField(max_length=100)
    currency = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    default_wallet = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(primary_key=True, max_length=16)

    class Meta:
        managed = False
        db_table = 'follow_wallet'


class LedgerCheckpoint(models.Model):
    coin = models.IntegerField(primary_key=True)
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ledger_checkpoint'


class LedgerEvent(models.Model):
    timestamp = models.BigIntegerField(blank=True, null=True)
    miner = models.CharField(max_length=100, blank=True, null=True)
    coin = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    transaction_status = models.IntegerField(blank=True, null=True)
    transaction_proposed_height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ledger_event'


class MinerStatus(models.Model):
    miner = models.CharField(primary_key=True, max_length=100)
    currency = models.CharField(max_length=8)
    mean_hashrate_24h = models.FloatField(blank=True, null=True)
    local_hashrate = models.FloatField(blank=True, null=True)
    mean_local_hashrate_24h = models.FloatField(blank=True, null=True)
    valid_shares_24h = models.IntegerField(blank=True, null=True)
    stale_shares_24h = models.IntegerField(blank=True, null=True)
    invalid_shares_24h = models.IntegerField(blank=True, null=True)
    online_worker_count = models.IntegerField(blank=True, null=True)
    offline_worker_count = models.IntegerField(blank=True, null=True)
    hashrate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'miner_status'
        unique_together = (('miner', 'currency'),)


class Subuser(models.Model):
    uuid = models.CharField(primary_key=True, max_length=16)
    user_uuid = models.ForeignKey('User', models.DO_NOTHING, db_column='user_uuid')
    name = models.CharField(unique=True, max_length=100)
    memo = models.CharField(max_length=100, blank=True, null=True)
    img_url = models.CharField(max_length=100, blank=True, null=True)
    id_open_account = models.IntegerField(blank=True, null=True)
    account_stat = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subuser'


class SubuserObserver(models.Model):
    subuser_uuid = models.ForeignKey(Subuser, models.DO_NOTHING, db_column='subuser_uuid')
    observer_user_uuid = models.ForeignKey('User', models.DO_NOTHING, db_column='observer_user_uuid')

    class Meta:
        managed = False
        db_table = 'subuser_observer'


class SubuserPaymentAddress(models.Model):
    white_list_uuid = models.ForeignKey(AddressWhiteList, models.DO_NOTHING, db_column='white_list_uuid')
    subuser_uuid = models.ForeignKey(Subuser, models.DO_NOTHING, db_column='subuser_uuid')
    percent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subuser_payment_address'


class User(models.Model):
    uuid = models.CharField(primary_key=True, max_length=16)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.TextField()
    phone = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class WorkerStatus(models.Model):
    miner = models.CharField(max_length=100)
    worker = models.CharField(max_length=100)
    currency = models.CharField(primary_key=True, max_length=8)
    hashrate = models.FloatField(blank=True, null=True)
    mean_hashrate_24h = models.FloatField(blank=True, null=True)
    local_hashrate = models.FloatField(blank=True, null=True)
    mean_local_hashrate_24h = models.FloatField(blank=True, null=True)
    mean_hashrate_diff = models.FloatField(blank=True, null=True)
    valid_shares = models.IntegerField(blank=True, null=True)
    stale_shares = models.IntegerField(blank=True, null=True)
    invalid_shares = models.IntegerField(blank=True, null=True)
    valid_shares_24h = models.IntegerField(blank=True, null=True)
    stale_shares_24h = models.IntegerField(blank=True, null=True)
    invalid_shares_24h = models.IntegerField(blank=True, null=True)
    stale_rate = models.FloatField(blank=True, null=True)
    invalid_rate = models.FloatField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    last_report_time = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worker_status'
