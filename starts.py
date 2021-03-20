import requests
import json
from abc import ABC
from abc import abstractmethod
from functools import wraps

def get_daily_json():  # updates JSON with different currencies values
	resp = requests.get(
		'https://www.cbr-xml-daily.ru/daily_json.js'
		)
	with open('request_result.json', 'w', encoding='utf8') as handler:
		json.dump(resp.json(), handler, indent=4, ensure_ascii=False)

def update(func):  # wrapper. Runs get_daily_json inb4 func
	@wraps(func)
	def wrap(*args, **kwargs):
		print('Updating daily JSON...')
		get_daily_json()
		print(f'Daily JSON updated. running {func.__name__} function.')
		func(*args, **kwargs)
		print(f'Function {func.__name__} stopped running.')
		return func(*args, **kwargs)
	return wrap

class Currency(ABC):  # abstract class, describes currency
	def __init__(self, amount):
		super().__init__()
		self.amount = float(amount)
		self._output = self.get_rub_value()
		self.rub_value = self._output[0]*self.amount
		self.prev_rub_value = self._output[1]*self.amount
		self.diff = self._output[0] - self._output[1]

	@update
	def get_rub_value(self):  # parses JSON to get rouble equivalents
		with open('request_result.json', 'r', encoding='utf8') as handler:
			cb_dict = json.load(handler)

		rub_value = cb_dict['Valute'][self.CHAR_CODE]['Value']
		prev_rub_value = cb_dict['Valute'][self.CHAR_CODE]['Previous']
		return [rub_value, prev_rub_value]

	def update():
		get_daily_json()


class Dollar(Currency):
	CHAR_CODE = 'USD'
	#def __init__(self, amount):
	#	super().__init__(amount)

class Euro(Currency):
	CHAR_CODE = 'EUR'
	#def __init__(self, amount):
	#	super().__init__(amount)


#commit test

