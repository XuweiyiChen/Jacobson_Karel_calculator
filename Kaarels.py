class Jacobson_Karel_calculator:

    def __init__(self, sigma, estimateRTT, deviation):
        self.sampleRTT = 1
        self.sigma = sigma
        self.estimateRTT = estimateRTT
        self.deviation = deviation
        self.iteration = 1

    def calculate(self):
        difference = self.sampleRTT - self.estimateRTT
        time_out = self.estimateRTT + 4 * self.deviation
        while time_out > 4:
            self.estimateRTT = self.estimateRTT + float(self.sigma * difference)
            self.deviation = self.deviation + float(self.sigma * (abs(difference) - self.deviation))
            difference = self.sampleRTT - self.estimateRTT
            time_out = self.estimateRTT + 4 * self.deviation
            self.iteration += 1
            print(self.sampleRTT, self.estimateRTT, self.deviation, difference, time_out)
        return self.iteration
