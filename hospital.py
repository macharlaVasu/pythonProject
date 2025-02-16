from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from snowflake_connection import create_snowflake_connection




class Hospital:
    def __init__(self,root):
        self.root=root 
        self.root.title("Macharla's Hospital Mannagement Sytemt")
        self.root.geometry("1540x800+0+0")

        self.NameOfTablets =StringVar()
        self.ref =StringVar()
        self.NumberOfTablets =StringVar()
        self.Dose =StringVar()
        self.Lots =StringVar()
        self.DateOfIssue =StringVar()
        self.DateOfExp =StringVar()
        self.dailyDose =StringVar()
        self.sideEffect =StringVar()
        self.FutureInfo =StringVar()
        self.BloodPressure =StringVar()
        self.StorageAd =StringVar()
        self.Medication =StringVar()
        self.PatientId =StringVar()
        self.NhsNumber =StringVar()
        self.PatientName =StringVar()
        self.DOB =StringVar()
        self.PatientAddress =StringVar()

        








        # Label creation 
        lbltitle =Label(self.root,
                        bd=20,
                        relief=RIDGE,
                        text="KRITHIK & TAKSHIV HOSPITAL MANAGEMENT SYSTEM",
                        fg='red',bg='white',
                        font=("time new roman",50,"bold")
                        )
        
        
        lbltitle.pack(side=TOP,fill=X)

        #===================Data frame ===========================================================================
        DataFrame =Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1540,height=400)

        
        DataFrameLeft =LabelFrame(DataFrame,
                                  bd=10,
                                  padx=20,
                                  relief=RIDGE,
                                  font=("arial",20,"bold"),
                                  text="Patient Information")
        
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight =LabelFrame(DataFrame,
                                  bd=10,
                                  padx=20,
                                  relief=RIDGE,
                                  font=("arial",20,"bold"),
                                  text="Prescription")
        
        DataFrameRight.place(x=990,y=5,width=460,height=350)

        # =============== Button Frames =======================================================================

        ButtonFrame =Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1530,height=70)

        
        # =============== Details  Frames =======================================================================

        DetailsFrame =Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=600,width=1540,height=200)

        # ================= dataFrame Names left =================================================================
         
        lblnameTablet =Label(DataFrameLeft,
                             text="Name of the Tablet : ",
                             font=("time new roman",12,"bold"),
                             padx=2,
                             pady=6)
        lblnameTablet.grid(row=0,column=0,sticky=W) 

        comNameTablet = ttk.Combobox(DataFrameLeft,textvariable=self.NameOfTablets,state="readonly",font=("time new roman",12,"bold"),width=33)
        comNameTablet["values"]=("Nice","Corona Vacacine","Acetaminophen","Aspirin","Ibuprofen","Naproxen")
        comNameTablet.grid(row=0,column=1)

        lblref =Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No : ",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.ref)
        txtref.grid(row=1,column=1,sticky=W)

        lbldose =Label(DataFrameLeft,font=("arial",12,"bold"),text="DOSE : ",padx=2,pady=4)
        lbldose.grid(row=2,column=0,sticky=W)
        txtdose = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.Dose)
        txtdose.grid(row=2,column=1,sticky=W)

        lblNoOfTablets =Label(DataFrameLeft,font=("arial",12,"bold"),text="No Of Tablets : ",padx=2,pady=4)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablest= Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.NumberOfTablets)
        txtNoOfTablest.grid(row=3,column=1,sticky=W)

        lblLots =Label(DataFrameLeft,font=("arial",12,"bold"),text="Lots : ",padx=2,pady=4)
        lblLots.grid(row=4,column=0,sticky=W)
        txtLots= Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.Lots)
        txtLots.grid(row=4,column=1,sticky=W)

        lblDoi =Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Of Issue : ",padx=2,pady=4)
        lblDoi.grid(row=5,column=0,sticky=W)
        txtDoi= Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.DateOfIssue)
        txtDoi.grid(row=5,column=1,sticky=W)

        lblDoe =Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Of Expiry : ",padx=2,pady=6)
        lblDoe.grid(row=6,column=0,sticky=W)
        txtDoe= Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.DateOfExp)
        txtDoe.grid(row=6,column=1,sticky=W)

        lblDailyDose =Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose : ",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose= Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.dailyDose)
        txtDailyDose.grid(row=7,column=1,sticky=W)

        lblSideEffects=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effects : ",padx=2,pady=6)
        lblSideEffects.grid(row=8,column=0,sticky=W)
        txtSideEffects= Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.sideEffect)
        txtSideEffects.grid(row=8,column=1,sticky=W)

        lblFurtureInfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Furture Information : ",padx=2,pady=6)
        lblFurtureInfo.grid(row=0,column=2,sticky=W)
        txtFurtureInfo= Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.FutureInfo)
        txtFurtureInfo.grid(row=0,column=3,sticky=W)

        lblBloodPre=Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure : ",padx=2,pady=6)
        lblBloodPre.grid(row=1,column=2,sticky=W)
        txtBloodPre= Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.BloodPressure)
        txtBloodPre.grid(row=1,column=3,sticky=W)

        lblStorageAd=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice: ",padx=2,pady=6)
        lblStorageAd.grid(row=2,column=2,sticky=W)
        txtStorageAd= Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.StorageAd)
        txtStorageAd.grid(row=2,column=3,sticky=W)

        lblMedication=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medication : ",padx=2,pady=6)
        lblMedication.grid(row=3,column=2,sticky=W)
        txtMedication= Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.Medication)
        txtMedication.grid(row=3,column=3,sticky=W)

        lblPatientID=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient ID: ",padx=2,pady=6)
        lblPatientID.grid(row=4,column=2,sticky=W)
        txtPatientID= Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.PatientId)
        txtPatientID.grid(row=4,column=3,sticky=W)

        lblNHSno=Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS Number: ",padx=2,pady=6)
        lblNHSno.grid(row=5,column=2,sticky=W)
        txtNHSno= Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.NhsNumber)
        txtNHSno.grid(row=5,column=3,sticky=W)

        lblPatName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name: ",padx=2,pady=6)
        lblPatName.grid(row=6,column=2,sticky=W)
        txtPatName=  Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.PatientName)
        txtPatName.grid(row=6,column=3,sticky=W)

        lblDOB=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Of Birth: ",padx=2,pady=6)
        lblDOB.grid(row=7,column=2,sticky=W)
        txtDOB= Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.DOB)
        txtDOB.grid(row=7,column=3,sticky=W)

        lblPatAdd=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Address: ",padx=2,pady=6)
        lblPatAdd.grid(row=8,column=2,sticky=W)
        txtPatAdd =Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,textvariable=self.PatientAddress)
        txtPatAdd.grid(row=8,column=3,sticky=W)


        # ================   Data Frame names right ==========================================================

        self.txtPrescription = Text(DataFrameRight,font=("arial",15,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        # ================================Button=========================================================

        btnPrescription = Button(ButtonFrame,text="Prescription",fg='green',bg='white',
                                 font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionDetails = Button(ButtonFrame,fg='green',bg='white',
                                        text="Prescription Data",
                                        command=self.iPrescriptionData,
                                        font=("arial",12,"bold"),
                                        width=23,padx=2,pady=6)
        btnPrescriptionDetails.grid(row=0,column=1)


        btnUpdate= Button(ButtonFrame,text="Update",fg='green',bg='white',
                          font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)
                       

        btnDelete = Button(ButtonFrame,text="Delete",fg='green',bg='white',
                           font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnInsert = Button(ButtonFrame,text="Clear",fg='green',bg='white',
                           font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnInsert.grid(row=0,column=4)

        btnExit = Button(ButtonFrame,text="Exit",fg='green',bg='white',
                         font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnInsert.grid(row=0,column=5)

        # ========================== Table ============================================================
        # ===============================Scroll Bar====================================================
        scroll_x = Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y = Scrollbar(DetailsFrame,orient=VERTICAL) 

        self.hospital_table = ttk.Treeview(DetailsFrame,
                                           columns=("nameoftable","ref",
                                                    "dose","nooftablets",
                                                    "lots","issuedate",
                                                    "expdate","dailydose",
                                                    # "sideeffect","futureinfo",
                                                    # "bloodpressure","medication","pateintid",
                                                    "storage","nhmnumber",
                                                    "pname","dob","address"))
        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x =ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y =ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name Of Tablets")
        self.hospital_table.heading("ref",text="Reference No")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lots",text="Lots")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Expiry Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        # self.hospital_table.heading("sideeffect",text="Side Effect")
        # self.hospital_table.heading("futureinfo",text="Future Information")
        # self.hospital_table.heading("bloodpressure",text="Blood Pressure")
        # self.hospital_table.heading("medication",text="Medication")
        # self.hospital_table.heading("pateintid",text="Patient ID")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhmnumber",text="NHM Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="Date Of Birth")
        self.hospital_table.heading("address",text="Patient Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftable",width=50)
        self.hospital_table.column("ref",width=50)
        self.hospital_table.column("dose",width=50)
        self.hospital_table.column("nooftablets",width=50)
        self.hospital_table.column("lots",width=50)
        self.hospital_table.column("issuedate",width=50)
        self.hospital_table.column("expdate",width=50)
        self.hospital_table.column("dailydose",width=50)
        # self.hospital_table.column("sideeffect",width=50)
        # self.hospital_table.column("futureinfo",width=50)
        # self.hospital_table.column("bloodpressure",width=50)
        # self.hospital_table.column("medication",width=50)
        # self.hospital_table.column("pateintid",width=50)
        self.hospital_table.column("storage",width=50)
        self.hospital_table.column("nhmnumber",width=50)
        self.hospital_table.column("pname",width=50)
        self.hospital_table.column("dob",width=50)
        self.hospital_table.column("address",width=50)

        self.hospital_table.pack(fill=BOTH,expand=1)

        # ============Functional declaration =========================

    def iPrescriptionData(self):
        if self.NumberOfTablets.get() == '' or self.ref.get() == '':
            messagebox.showerror("Error", "All Fields are Required")
        else:
            try:
                conn = create_snowflake_connection()
                my_cursor = conn.cursor()

                # Snowflake INSERT statement - Make sure your column count matches the placeholders
                query = """ 
                INSERT INTO hospital_details 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

                # Execute query with values extracted from StringVar using .get()
                my_cursor.execute(query, (
                    self.NameOfTablets.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    self.NumberOfTablets.get(),
                    self.Lots.get(),
                    self.DateOfIssue.get(),
                    self.DateOfExp.get(),
                    self.dailyDose.get(),
                    self.sideEffect.get(),
                    self.FutureInfo.get(),
                    self.BloodPressure.get(),
                    self.StorageAd.get(),
                    self.Medication.get(),
                    self.PatientId.get(),
                    self.NhsNumber.get(),
                    self.PatientName.get(),
                    self.DOB.get(),
                    self.PatientAddress.get()
                ))

                conn.commit()
                my_cursor.close()
                conn.close()

                messagebox.showinfo("Success", "Record has been inserted successfully")

            except Exception as e:
                messagebox.showerror("Database Error", f"Failed to insert record: {e}")



        
            





root =Tk()
hosobj = Hospital(root)

root.mainloop()
       
    