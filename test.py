from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Macharla's Hospital Management System")
        self.root.geometry("1540x800+0+0")

        # Label creation
        lbltitle = Label(
            self.root,
            bd=20,
            relief=RIDGE,
            text="KRITHIK & TAKSHIV HOSPITAL MANAGEMENT SYSTEM",
            fg="red",
            bg="white",
            font=("times new roman", 50, "bold"),
        )
        lbltitle.pack(side=TOP, fill=X)

        # =================== Data frame ===========================================================================
        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1540, height=400)

        DataFrameLeft = LabelFrame(
            DataFrame,
            bd=10,
            padx=20,
            relief=RIDGE,
            font=("arial", 20, "bold"),
            text="Patient Information",
        )
        DataFrameLeft.place(x=0, y=5, width=980, height=350)

        DataFrameRight = LabelFrame(
            DataFrame,
            bd=10,
            padx=20,
            relief=RIDGE,
            font=("arial", 20, "bold"),
            text="Prescription",
        )
        DataFrameRight.place(x=990, y=5, width=460, height=350)

        # =============== Button Frames =======================================================================
        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(x=0, y=530, width=1530, height=70)

        # =============== Details Frames =======================================================================
        DetailsFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailsFrame.place(x=0, y=600, width=1540, height=200)

        # ================= dataFrame Names left =================================================================
        lblnameTablet = Label(
            DataFrameLeft,
            text="Name of the Tablet : ",
            font=("times new roman", 12, "bold"),
            padx=2,
            pady=6,
        )
        lblnameTablet.grid(row=0, column=0, sticky=W)

        comNameTablet = ttk.Combobox(
            DataFrameLeft, state="readonly", font=("times new roman", 12, "bold"), width=33
        )
        comNameTablet["values"] = (
            "Nice",
            "Corona Vaccine",
            "Acetaminophen",
            "Aspirin",
            "Ibuprofen",
            "Naproxen",
        )
        comNameTablet.grid(row=0, column=1)

        lblref = Label(
            DataFrameLeft, font=("arial", 12, "bold"), text="Reference No : ", padx=2
        )
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=1, column=1, sticky=W)

        lbldose = Label(
            DataFrameLeft, font=("arial", 12, "bold"), text="DOSE : ", padx=2, pady=4
        )
        lbldose.grid(row=2, column=0, sticky=W)
        txtdose = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtdose.grid(row=2, column=1, sticky=W)

        lblNoOfTablets = Label(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            text="No Of Tablets : ",
            padx=2,
            pady=4,
        )
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablest = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtNoOfTablest.grid(row=3, column=1, sticky=W)

        lblLots = Label(
            DataFrameLeft, font=("arial", 12, "bold"), text="Lots : ", padx=2, pady=4
        )
        lblLots.grid(row=4, column=0, sticky=W)
        txtLots = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtLots.grid(row=4, column=1, sticky=W)

        lblDoi = Label(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            text="Date Of Issue : ",
            padx=2,
            pady=4,
        )
        lblDoi.grid(row=5, column=0, sticky=W)
        txtDoi = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtDoi.grid(row=5, column=1, sticky=W)

        lblDoe = Label(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            text="Date Of Expiry : ",
            padx=2,
            pady=6,
        )
        lblDoe.grid(row=6, column=0, sticky=W)
        txtDoe = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtDoe.grid(row=6, column=1, sticky=W)

        lblDailyDose = Label(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            text="Daily Dose : ",
            padx=2,
            pady=6,
        )
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtDailyDose.grid(row=7, column=1, sticky=W)

        lblSideEffects = Label(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            text="Side Effects : ",
            padx=2,
            pady=6,
        )
        lblSideEffects.grid(row=8, column=0, sticky=W)
        txtSideEffects = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtSideEffects.grid(row=8, column=1, sticky=W)

        lblFurtureInfo = Label(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            text="Future Information : ",
            padx=2,
            pady=6,
        )
        lblFurtureInfo.grid(row=0, column=2, sticky=W)
        txtFurtureInfo = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtFurtureInfo.grid(row=0, column=3, sticky=W)

        lblBloodPre = Label(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            text="Blood Pressure : ",
            padx=2,
            pady=6,
        )
        lblBloodPre.grid(row=1, column=2, sticky=W)
        txtBloodPre = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtBloodPre.grid(row=1, column=3, sticky=W)

        lblStorageAd = Label(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            text="Storage Advice: ",
            padx=2,
            pady=6,
        )
        lblStorageAd.grid(row=2, column=2, sticky=W)
        txtStorageAd = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtStorageAd.grid(row=2, column=3, sticky=W)

        lblMedication = Label(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            text="Medication : ",
            padx=2,
            pady=6,
        )
        lblMedication.grid(row=3, column=2, sticky=W)
        txtMedication = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtMedication.grid(row=3, column=3, sticky=W)

        lblPatientID = Label(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            text="Patient ID: ",
            padx=2,
            pady=6,
        )
        lblPatientID.grid(row=4, column=2, sticky=W)
        txtPatientID = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtPatientID.grid(row=4, column=3, sticky=W)

        lblNHSno = Label(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            text="NHS Number: ",
            padx=2,
            pady=6,
        )
        lblNHSno.grid(row=5, column=2, sticky=W)
        txtNHSno = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtNHSno.grid(row=5, column=3, sticky=W)

        lblPatName = Label(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            text="Patient Name: ",
            padx=2,
            pady=6,
        )
        lblPatName.grid(row=6, column=2, sticky=W)
        txtPatName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtPatName.grid(row=6, column=3, sticky=W)

        lblDOB = Label(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            text="Date Of Birth: ",
            padx=2,
            pady=6,
        )
        lblDOB.grid(row=7, column=2, sticky=W)
        txtDOB = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtDOB.grid(row=7, column=3, sticky=W)

        lblPatAdd = Label(
            DataFrameLeft,
            font=("arial", 12, "bold"),
            text="Patient Address: ",
            padx=2,
            pady=6,
        )
        lblPatAdd.grid(row=8, column=2, sticky=W)
        txtPatAdd = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtPatAdd.grid(row=8, column=3, sticky=W)

        # ================ Data Frame names right ==========================================================
        self.txtPrescription = Text(
            DataFrameRight, font=("arial", 15, "bold"), width=45, height=16, padx=2, pady=6
        )
        self.txtPrescription.grid(row=0, column=0)

        # ================================ Button =========================================================
        btnPrescription = Button(
            ButtonFrame,
            text="Prescription",
            bg="green",  # Background color
            fg="white",  # Foreground (text) color
            font=("arial", 12, "bold"),
            width=23,
            padx=2,
            pady=6,
        )
        btnPrescription.grid(row=0, column=0)


# Main program
root = Tk()
hosobj = Hospital(root)
root.mainloop()