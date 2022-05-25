# eel-vue3-bootstrap
 template for using eel, python, vue3 and bootstrap together

# notes

Vue mounted calls the vue method `toPy_print`, which sends the call with argument to python and executes it. the return value is retVal.<br/>
Python executes `fromPy_alert` which is exposed in js but does **not** belong to vue. That method then calls a vue method. maybe this can be shortened in eel? In any case, its considered "anti-pattern" and should be avoided if possible. Since js->python calls can have a return, most things can be handled that way. if you need python to update js dynamically, then you have to use this anti-pattern.