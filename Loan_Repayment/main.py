from flask import Flask,render_template,request
import pickle
app=Flask(__name__)

@app.route('/',methods=['GET'])
def HomePage():
 return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def index():
 if request.method=='POST':
  try:
   cred_policy = int(request.form['cred_policy'])
   Interest   = float(request.form['Interest'])
   installment = float(request.form['installment'])
   Annual_Income = float(request.form['Annual_Income'])
   dti_ratio = float(request.form['dti_ratio'])
   fico = int(request.form['fico'])
   Cred_line = float(request.form['Cred_line'])
   revol_bal = float(request.form['revol_bal'])
   revol_util = float(request.form['revol_util'])
   inq_6_mnths = float(request.form['inq_6_mnths'])
   deal_2_yrs = float(request.form['deal_2_yrs'])
   pub_rcrd  = float(request.form['pub_rcrd'])
   card_hldr  = int(request.form['card_hldr'])
   debt_consol  = int(request.form['debt_consol'])
   educ  = int(request.form['educ'])
   hme_improv  = int(request.form['hme_improv'])
   mjr_purpse  = int(request.form['mjr_purpse'])
   smll_busnes  = int(request.form['smll_busnes'])


   filename = 'finalized_model.sav'
   print('Hi There')
   loaded_model = pickle.load(open(filename, 'rb'))


   import numpy as np
   print('Hi')
   prediction=loaded_model.predict([[cred_policy,Interest,installment,Annual_Income,dti_ratio,fico,Cred_line,revol_bal,revol_util,
                                     inq_6_mnths,deal_2_yrs,pub_rcrd,card_hldr,debt_consol,educ,hme_improv,mjr_purpse,smll_busnes]])
   print(prediction)
   for i in prediction:
    if i==1:
     prediction='will repay'
    else:
     prediction='willnot be able to repay'


   return render_template('results.html',prediction=prediction)
  except Exception as e:
    print('The Exception message is: ',e)
    return 'something is wrong'
 else:
  return render_template('index.html'),

if __name__ == "__main__":
    app.run()
