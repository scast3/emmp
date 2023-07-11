class pump:
    #Defined by Class 'P' in EAM
    def __init__(self,pump_number,pump_name,manufacturer, serial_number,commission_date,location,efficiency,speed,q,h,specific_weight):
        self.pump_number = pump_number
        self.pump_name = pump_name
        self.manufacturer = manufacturer
        self.serial_number = serial_number
        self.commission_date = commission_date
        self.location = location
        self.speed = speed #RPM
        self.n = efficiency #BEP efficiency, needs to be retrieved from pump curve
        self.q = q #capacity/flow (GPM)
        self.h = h #pump head (ft)
        self.specifc_weight = specific_weight

        self.whp = q*h*specific_weight/3960
        self.bhp = self.whp/self.n

        self.motor_n = -1
            
    #motor and transmission efficiencies stay the same in pump replacement
        
    def cost(self,rate):
        c = 0.746 * self.q * self.h * rate/(3960*self.n*self.motor_n)

    def total_efficiency(self,total_cost,rate):
        n = 0.746 * self.q * self.h * rate/(total_cost*3960)
    #def find_n_motor(self):
        
class comparison:

    def __init__(self,pump1,pump2):
        self.old_pump = pump1
        self.new_pump = pump2

    def compare_efficiency(self)

    def compare_cost(self)