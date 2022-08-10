from django.db import models

class Production052022Shift(models.Model):
    machine_id = models.IntegerField()
    mill_date = models.DateTimeField()
    mill_shift = models.IntegerField(null=False)
    total_products = models.BigIntegerField()
    total_run_time = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    total_losses = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    total_loss_1 = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    total_loss_2 = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    total_target = models.FloatField(blank=True, null=True)
    total_actual = models.FloatField(blank=True, null=True)
    total_goodqty = models.FloatField(blank=True, null=True)
    total_errorqty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_052022_shift'