from flask import Flask, render_template, request
from datetime import date
from pandas import pandas as pd
import xgboost as xgb
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Calculations and result code
@app.route('/result', methods=['POST'])
def result():
    # Random file extension searching code to allow transferability
    my_dir = os.path.dirname(__file__)
    json_pathway = os.path.join(my_dir, 'fast_nonfast_0mos_6mos.json')
    # To get all the posted information
    var_gender = request.form['Gender']
    var_bulbar = request.form['Bulbar']
    var_limb = request.form['Limb']
    var_riluzole = request.form['Riluzole']
    var_bmi = request.form['Bmi']
    var_pulse = request.form['Pulse']
    var_rr = request.form['Rr']
    var_dbp = request.form['Dbp']
    var_sbp = request.form['Sbp']
    var_fvc = request.form['Fvc']
    var_alt = request.form['Alt']
    var_ast = request.form['Ast']
    var_uric = request.form['Uric']
    var_bun = request.form['Bun']
    var_alb = request.form['Alb']
    var_anc = request.form['Anc']
    var_protein = request.form['Protein']
    var_ck = request.form['Ck']
    var_tchol = request.form['Tchol']
    var_tg = request.form['Tg']
    var_hba1c = request.form['Hba1c']
    var_hb = request.form['Hb']
    var_hct = request.form['Hct']
    var_wbc = request.form['Wbc']
    var_rbc = request.form['Rbc']
    var_cr = request.form['Cr']
    var_na = request.form['Sodium']
    var_k = request.form['Potassium']
    var_cl = request.form['Chloride']
    var_glu = request.form['Glucose']
    var_plt = request.form['Platelets']
    var_abseos = request.form['Abseos']
    var_alp = request.form['Alp']
    var_bicarb = request.form['Bicarbonate']
    var_ca = request.form['Calcium']
    var_abslym = request.form['Abslym']
    var_absmon = request.form['Absmon']
    var_absbas = request.form['Absbas']
    var_tbil = request.form['Tbil']
    var_ggt = request.form['Ggt']
    var_perlym = request.form['Perlym']
    var_permon = request.form['Permon']
    var_perbas = request.form['Perbas']
    var_po = request.form['Phosphorus']
    var_pereos = request.form['Pereos']
    var_alsfsr = request.form['Alsfrsr']
    var_alsfsrslp = request.form['Alsfrsrslp']
    var_advtot = request.form['Advtotal']
    var_advres = request.form['Advres']
    var_advnem = request.form['Advnem']
    var_advpsy = request.form['Advpsy']
    var_advmet = request.form['Advmet']
    
    # Compute the onset time and age
    today = date.today()
    var_onset = date.fromisoformat(request.form['Onset'])
    delta_onset = var_onset - today
    delta_onset_days = delta_onset.days # Actual variable for onset
    var_diagnosis = date.fromisoformat(request.form['Diagnosis'])
    delta_diagnosis = var_diagnosis - today
    delta_diagnosis_days = delta_diagnosis.days # Actual variable for diagnosis
    var_birthday = date.fromisoformat(request.form['Birthday'])
    delta_birthday = today - var_birthday
    delta_birthday_days = delta_birthday.days
    var_age = delta_birthday_days / 365.25 # Actual variable for age
    
    try:
        # Rudimentary error checking to ensure only float or null inputs
        # Reason for if/else is to detect and allow for null inputs
        c_gender = float(var_gender)
        c_bulbar = float(var_bulbar)
        c_limb = float(var_limb)
        c_riluzole = float(var_riluzole)
        if var_bmi == '':
            c_bmi = float("nan")
        else:
            c_bmi = float(var_bmi)
        if var_pulse == '':
            c_pulse = float("nan")
        else:
            c_pulse = float(var_pulse)
        if var_rr == '':
            c_rr = float("nan")
        else:
            c_rr = float(var_rr)
        if var_dbp == '':
            c_dbp  = float("nan")
        else:
            c_dbp  = float(var_dbp)
        if var_sbp == '':
            c_sbp = float("nan")
        else:
            c_sbp = float(var_sbp)
        if var_fvc == '':
            c_fvc = float("nan")
        else:
            c_fvc = float(var_fvc)
        if var_alt == '':
            c_alt = float("nan")
        else:
            c_alt = float(var_alt)
        if var_ast == '':
            c_ast = float("nan")
        else:
            c_ast = float(var_ast)
        if var_uric == '':
            c_uric = float("nan")
        else:
            c_uric = float(var_uric)
        if var_bun == '':
            c_bun = float("nan")
        else:
            c_bun = float(var_bun)
        if var_alb == '':
            c_alb = float("nan")
        else:
            c_alb = float(var_alb)
        if var_anc == '':
            c_anc = float("nan")
        else:
            c_anc = float(var_anc)
        if var_protein == '':
            c_protein = float("nan")
        else:
            c_protein = float(var_protein)
        if var_ck == '':
            c_ck = float("nan")
        else:
            c_ck = float(var_ck)
        if var_tchol == '':
            c_tchol = float("nan")
        else:
            c_tchol = float(var_tchol)
        if var_tg == '':
            c_tg = float("nan")
        else:
            c_tg = float(var_tg)
        if var_hba1c == '':
            c_hba1c = float("nan")
        else:
            c_hba1c = float(var_hba1c)
        if var_hb == '':
            c_hb = float("nan")
        else:
            c_hb = float(var_hb)
        if var_hct == '':
            c_hct = float("nan")
        else:
            c_hct = float(var_hct)
        if var_wbc == '':
            c_wbc = float("nan")
        else:
            c_wbc = float(var_wbc)
        if var_rbc == '':
            c_rbc = float("nan")
        else:
            c_rbc = float(var_rbc)
        if var_cr == '':
            c_cr = float("nan")
        else:
            c_cr = float(var_cr)
        if var_na == '':
            c_na = float("nan")
        else:
            c_na = float(var_na)
        if var_k == '':
            c_k = float("nan")
        else:
            c_k = float(var_k)
        if var_cl == '':
            c_cl = float("nan")
        else:
            c_cl = float(var_cl)
        if var_glu == '':
            c_glu = float("nan")
        else:
            c_glu = float(var_glu)
        if var_plt == '':
            c_plt = float("nan")
        else:
            c_plt = float(var_plt)
        if var_abseos == '':
            c_abseos = float("nan")
        else:
            c_abseos = float(var_abseos)
        if var_alp == '':
            c_alp = float("nan")
        else:
            c_alp = float(var_alp)
        if var_bicarb == '':
            c_bicarb = float("nan")
        else:
            c_bicarb = float(var_bicarb)
        if var_ca == '':
            c_ca = float("nan")
        else:
            c_ca = float(var_ca)
        if var_abslym == '':
            c_abslym = float("nan")
        else:
            c_abslym = float(var_abslym)
        if var_absmon == '':
            c_absmon = float("nan")
        else:
            c_absmon = float(var_absmon)
        if var_absbas == '':
            c_absbas = float("nan")
        else:
            c_absbas = float(var_absbas)
        if var_tbil == '':
            c_tbil = float("nan")
        else:
            c_tbil = float(var_tbil)
        if var_ggt == '':
            c_ggt = float("nan")
        else:
            c_ggt = float(var_ggt)
        if var_perlym == '':
            c_perlym = float("nan")
        else:
            c_perlym = float(var_perlym)
        if var_permon == '':
            c_permon = float("nan")
        else:
            c_permon = float(var_permon)
        if var_perbas == '':
            c_perbas = float("nan")
        else:
            c_perbas = float(var_perbas)
        if var_po == '':
            c_po = float("nan")
        else:
            c_po = float(var_po)
        if var_pereos == '':
            c_pereos = float("nan")
        else:
            c_pereos = float(var_pereos)
        if var_alsfsr == '':
            c_alsfsr = float("nan")
        else:
            c_alsfsr = float(var_alsfsr)
        if var_alsfsrslp == '':
            c_alsfsrslp = float("nan")
        else:
            c_alsfsrslp = float(var_alsfsrslp)
        if var_advtot == '':
            c_advtot = float("nan")
        else:
            c_advtot = float(var_advtot)
        if var_advres == '':
            c_advres = float("nan")
        else:
            c_advres = float(var_advres)
        if var_advnem == '':
            c_advnem = float("nan")
        else:
            c_advnem = float(var_advnem)
        if var_advpsy == '':
            c_advpsy = float("nan")
        else:
            c_advpsy = float(var_advpsy)
        if var_advmet == '':
            c_advmet = float("nan")
        else:
            c_advmet = float(var_advmet)
        # Error handling for bad inputs
    except ValueError:
        return render_template(
        'index.html', 
        validation=False
        ) 
    else:
        # Convert to pandas dataframe
        dataframe = pd.DataFrame(
            {
                'Onset_Delta':[delta_onset_days],
                'Diagnosis_Delta':[delta_diagnosis_days],
                'Age':[var_age],
                'Sex':[c_gender],
                'site_bulbar':[c_bulbar],
                'site_limb':[c_limb],
                'RiluzoleUse':[c_riluzole],
                'BMI':[c_bmi],
                'Pulse':[c_pulse],
                'Respiratory_Rate':[c_rr],
                'BP_Diastolic':[c_dbp],
                'BP_Systolic':[c_sbp],
                'FVC_perc_new':[c_fvc],
                'ALT':[c_alt],
                'AST':[c_ast],
                'UricAcid':[c_uric],
                'BUN':[c_bun],
                'Albumin':[c_alb],
                'AbsNeutroCount':[c_anc],
                'Protein':[c_protein],
                'CK':[c_ck],
                'TotCholesterol':[c_tchol],
                'Triglycerides':[c_tg],
                'HbA1c':[c_hba1c],
                'Hb':[c_hb],
                'Hematocrit':[c_hct],
                'WBC':[c_wbc],
                'RBC':[c_rbc],
                'Creatinine':[c_cr],
                'Sodium':[c_na],
                'Potassium':[c_k],
                'Chloride':[c_cl],
                'Glucose':[c_glu],
                'Platelets':[c_plt],
                'AbsEosinophil':[c_abseos],
                'AlkalinePhosphatase':[c_alp],
                'Bicarbonate':[c_bicarb],
                'Calcium':[c_ca],
                'AbsLymphocyte':[c_abslym],
                'AbsMonocyte':[c_absmon],
                'AbsBasophil':[c_absbas],
                'BilirubinTotal':[c_tbil],
                'GGT':[c_ggt], 
                'PercLymphocytes':[c_perlym],
                'PercMonocytes':[c_permon],
                'PercBasophils':[c_perbas],
                'Phosphorus':[c_po],
                'PercEosinophils':[c_pereos],
                'alsfrsr':[c_alsfsr],
                'alsfrsr_slope':[c_alsfsrslp],
                'Adv_Total':[c_advtot],
                'Adv_Resp':[c_advres],
                'Adv_Nerv':[c_advnem],
                'Adv_Psych':[c_advpsy],
                'Adv_Metab':[c_advmet]
            })

        # Load model and evaluate
        booster = xgb.Booster()
        booster.load_model(json_pathway)
        dtmp = xgb.DMatrix(data=dataframe)
        result = booster.predict(dtmp)
        # Output
        return render_template(
        'index.html', 
        result=result,
        validation=True
        ) 
    
@app.route('/about')
def about ():
    return render_template('about.html')
    
if __name__ == '__main__':
    app.debug = True
    app.run()