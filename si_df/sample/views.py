from datetime import datetime
import imp
from re import I
from rest_framework import response,status
from django.shortcuts import render
from django.db import connection, router
from .models import Production052022Shift
from .serializer import *
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
# Create your views here.

cur=connection.cursor()

class ProductionView(GenericAPIView):
    serializer_class=ReportSerailizer
    print(serializer_class)

    def get(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            cur=connection.cursor()
            response_data={}
            response_data["is_error"]=False
            response_data["message"]="Process Complete"

            if serializer.data["period"].lower()=="shift":
                cur.execute("select * from production_052022_shift where substring(mill_date,1,10)=%s and mill_shift=%s",[serializer.data["from_mill_date"],
                                                                                                                            serializer.data["mill_shift"]])
                val_list=cur.fetchall()
            # print(val[0])
                full_data=[]
                for i in val_list:
                    full_data.append(
                        {
                        "machine_id":i[0],
                        "mill_date":i[1],
                        "mill_shift":i[2],
                        "total_products":i[3],
                        "total_run_time":i[4],
                        "total_losses":i[5],
                        "total_loss_1":i[6],
                        "total_loss_2":i[7],
                        "total_actual":i[8],
                        "total_goodqty":i[9],
                        "total_errorqty":i[10]

                    }
                    )

                response_data["data"]=full_data  
            
            elif serializer.data["period"].lower()=="day":
                cur.execute("select * from production_052022_day where substring(mill_date,1,10)=%s",[serializer.data["from_mill_date"]])

                val_list=cur.fetchall()
                

                full_data=[]
                for val in val_list:
                    full_data.append(
                        {
                            "machine_id":val[0],
                            "mill_date":val[1],
                            "total_shift":val[2],
                            "total_products":val[3],
                            "total_run_time":val[4],
                            "total_losses":val[5],
                            "total_loss_1":val[6],
                            "total_loss_2":val[7],
                            "total_target":val[8],
                            "total_actual":val[9],
                            "total_goodqty":val[10],
                            "total_errorqty":val[11]
                        }
                    )

                
                response_data["data"]=full_data

            elif serializer.data["period"].lower()=="day_from_to":
                cur.execute("select * from production_052022_day where mill_date between %s and %s",[serializer.data["from_mill_date"],
                                                                                                        serializer.data["to_mill_date"]])   

                val_list=cur.fetchall()

                
                full_data=[
                    {
                            "machine_id":val[0],
                            "mill_date":val[1],
                            "total_shift":val[2],
                            "total_products":val[3],
                            "total_run_time":val[4],
                            "total_losses":val[5],
                            "total_loss_1":val[6],
                            "total_loss_2":val[7],
                            "total_target":val[8],
                            "total_actual":val[9],
                            "total_goodqty":val[10],
                            "total_errorqty":val[11]
                    }
                    for val in val_list
                ]

                response_data["data"]=full_data




            elif serializer.data["period"].lower()=="day_shift_from_to":
                # cur.execute("select distinct mill_date from production_052022_shift where mill_date between %s and %s and mill_shift=%s",[serializer.data["from_mill_date"],
                #                                                                                                         serializer.data["to_mill_date"],
                #                                                                                                         serializer.data["mill_shift"]])
                # date_set=cur.fetchall()

                # print(date_set)
                # print(date_set)
                cur.execute("select * from production_052022_shift where mill_date between %s and %s and mill_shift=%s",[serializer.data["from_mill_date"],
                                                                                                                        serializer.data["to_mill_date"],
                                                                                                                        serializer.data["mill_shift"]])    
                val_list=cur.fetchall()
                # print(val)   
                # response_data["mill_shift"]=serializer.data["mill_shift"]
                full_data=[]
                
                
                # for date in date_set:
                #     temp_data=[]
                for val in val_list:
                # if date[0]==val[1]:
                    full_data.append(
                                {
                        "machine_id":val[0],
                        "mill_date":val[1],
                        "mill_shift":val[2],
                        "total_products":val[3],
                        "total_run_time":val[4],
                        "total_losses":val[5],
                        "total_loss_1":val[6],
                        "total_loss_2":val[7],
                        "total_target":val[8],
                        "total_goodqty":val[9],
                        "total_errorqty":val[10]

                        
                                }
                            )
                    

                response_data["data"]=full_data
            
            # val=Production052022Shift.objects.raw("select machine_id,mill_shift from production_052022_shift")
            
            return response.Response(response_data,status=status.HTTP_200_OK)
        # print(serializer.data)
        response_data={}
        response_data["is_error"]=True
        response_data["message"]="Invalid Parameters"
        response_data["data"]=[]

        return response.Response(response_data,status=status.HTTP_400_BAD_REQUEST)        

