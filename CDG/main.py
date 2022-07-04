
from js import alert
import string
def buttonFuncGetChecksum(*args,**kwargs):
 console.log('[DEUBG] function called')
 twelveDigitCode = Element('userinputchecksum').element.value
 if twelveDigitCode == "":
  Element('error2').element.innerText = "Can't work with nothing."
  pyscript.write('checkDigit', "")
  pyscript.write('fullCode', "")
 elif any(c in string.ascii_letters for c in twelveDigitCode):
  Element('error2').element.innerText = 'Numbers only!'
  pyscript.write('checkDigit', "")
  pyscript.write('fullCode', "")
 elif any(c in string.punctuation for c in twelveDigitCode):
  Element('error2').element.innerText = 'Numbers only!'
  pyscript.write('checkDigit', "")
  pyscript.write('fullCode', "")
 elif any(c in string.whitespace for c in twelveDigitCode):
  Element('error2').element.innerText = 'Numbers only!'
  pyscript.write('checkDigit', "")
  pyscript.write('fullCode', "")
 elif len(twelveDigitCode) != 12:
  Element('error2').element.innerText = 'Twelve digit codes only!'
  pyscript.write('checkDigit', "")
  pyscript.write('fullCode', "")
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
  if checkNumber == 10:
   checkNumber = 0
  Element('error2').element.innerText = ''
  pyscript.write('checkDigit', checkNumber)
  pyscript.write('fullCode', twelveDigitCode + checkNumber)