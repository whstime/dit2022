#Imports
from js import alert
import string
from pyodide import create_proxy
#Set inputfield variable to gold DOM element
inputField = document.getElementById('userinputchecksum')
#Def function that checks if every key you type in the input field is 
# a enter and if it is a enter it calls on the buttonFuncGetChecksum
def keyDownFunc(e):
 if e.key == 'Enter':
  buttonFuncGetChecksum()
ckd = create_proxy(keyDownFunc)
inputField.addEventListener("keydown",ckd)
#Def function that takes what is in the input field checks if its usable/applicable and if nothing is 
# wrong it does the math to provide the user with the checksum digit which it does at the end
def buttonFuncGetChecksum(*args,**kwargs):
 console.log('[DEUBG] function called')
 #Gets the user input
 twelveDigitCode = Element('userinputchecksum').element.value
 #Error checks (e.g user put in a symbol instead of a number somwewhere)
 if twelveDigitCode == "":
  Element('error2').element.innerText = "Can't work with nothing."
  pyscript.write('checkDigit', "")
  pyscript.write('fullCode', "")
  Element('error').element.style.opacity = ''
  console.log('[DEBUG] Opacity for ERROR tag:', Element('error').element.style.opacity)
 elif any(c in string.ascii_letters for c in twelveDigitCode) or any(c in string.punctuation for c in twelveDigitCode) or any(c in string.whitespace for c in twelveDigitCode):
  Element('error2').element.innerText = 'Numbers only!'
  pyscript.write('checkDigit', "")
  pyscript.write('fullCode', "")
  Element('error').element.style.opacity = ''
  console.log('[DEBUG] Opacity for ERROR tag:', Element('error').element.style.opacity)
 elif len(twelveDigitCode) != 12:
  Element('error2').element.innerText = 'Twelve digit codes only!'
  pyscript.write('checkDigit', "")
  pyscript.write('fullCode', "")
  Element('error').element.style.opacity = ''
#Does what it is supposed to if it there are no errors apperent
 else:
  listOfDigits = [int(a) for a in str(twelveDigitCode)]
  Two = listOfDigits[1] * 3
  Four = listOfDigits[3] * 3
  Six = listOfDigits[5] * 3
  Eight = listOfDigits[7] * 3
  Ten = listOfDigits[9] * 3
  Twelve = listOfDigits[11] * 3
  sumResult = listOfDigits[0] + Two + listOfDigits[2] + Four + listOfDigits[4] + Six + listOfDigits[6] + Eight + listOfDigits[8] + Ten + listOfDigits[10] + Twelve
  sumList = [int(a) for a in str(sumResult)]
  checkNumber = str(10 - sumList[-1])
  #If the check number is 10 replaces it with
  if checkNumber == '10':
   console.log('[DEUBG: CHECKNUMBER IS 10')
   checkNumber = '0'
  else:
    #debug
   console.log('[DEUBG: CHECKNUMBER IS NOT 10')
  #DOM Manipulation
  Element('error2').element.innerText = ''
  Element('error').element.style.opacity = '0'
  console.log('[DEBUG]', Element('error').element.style.opacity)
  pyscript.write('checkDigit', checkNumber)
  pyscript.write('fullCode', twelveDigitCode + checkNumber)