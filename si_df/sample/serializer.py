from email.policy import default
from django.forms import ValidationError
from rest_framework import serializers


class ReportSerailizer(serializers.Serializer):
    mill_shift=serializers.IntegerField(default=None)
    period=serializers.CharField(default=None)
    from_mill_date=serializers.CharField(default=None)
    to_mill_date=serializers.CharField(default=None)

    class Meta:
        fields="__all__"

    def validate(self, data):
        if data["period"]==None:
            raise ValidationError("error")
        else:
            if data["period"].lower()=="shift":
                if data["from_mill_date"]==None or data["mill_shift"]==None:
                    raise ValidationError("error")
                return data
            
            elif data["period"].lower()=="day":
                if data["from_mill_date"]:
                    return data
                raise ValidationError("error")
                
            elif data["period"].lower()=="from_to":
                if data["from_mill_date"] and data["to_mill_date"] and data["mill_shift"]:
                    data["period"]="day_shift_from_to"
                    return data
                
                elif data["from_mill_date"] and data["to_mill_date"]:
                    data["period"]="day_from_to"
                    return data
                
                else:
                    raise ValidationError("error")

            # elif data["period"].lower()=="month":
            #     return data
        
            


