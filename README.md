# User-Activity-Api

# Requirements
1. Python 3
2. Django 3


# Set Up
1. Install Python3 in Your System.
2. Install all required pacakages from requirement.txt file .


# Custom Management Command Usage For Dummy Data in Database

To use Custom Management Command Use following :

python manage.py seed

The above command populate 100 user and 100 entry to the user_details and user_activity table respectively.


# API Usage and Endpoint(Local Server)

Note: This Endpoint is for localhost .

Url: http://127.0.0.1:8000/activity/  

Method: Get

Example Response Format :

		{
			"ok": true,
			"members": [{
					"id": "W012A3CDE",
					"real_name": "Egon Spengler",
					"tz": "America/Los_Angeles",
					"activity_periods": [{
							"start_time": "Feb 1 2020  1:33PM",
							"end_time": "Feb 1 2020 1:54PM"
						},
						{
							"start_time": "Mar 1 2020  11:11AM",
							"end_time": "Mar 1 2020 2:00PM"
						},
						{
							"start_time": "Mar 16 2020  5:33PM",
							"end_time": "Mar 16 2020 8:02PM"
						}
					]
				},
				{
					"id": "W07QCRPA4",
					"real_name": "Glinda Southgood",
					"tz": "Asia/Kolkata",
					"activity_periods": [{
							"start_time": "Feb 1 2020  1:33PM",
							"end_time": "Feb 1 2020 1:54PM"
						},
						{
							"start_time": "Mar 1 2020  11:11AM",
							"end_time": "Mar 1 2020 2:00PM"
						},
						{
							"start_time": "Mar 16 2020  5:33PM",
							"end_time": "Mar 16 2020 8:02PM"
						}
					]
				}
			]
		}



# API EndPoint of Hosted Server

URL: http://dubeysachin03.pythonanywhere.com/activity/

Method: Get

Example Response Format :

		{
			"ok": true,
			"members": [{
					"id": "W012A3CDE",
					"real_name": "Egon Spengler",
					"tz": "America/Los_Angeles",
					"activity_periods": [{
							"start_time": "Feb 1 2020  1:33PM",
							"end_time": "Feb 1 2020 1:54PM"
						},
						{
							"start_time": "Mar 1 2020  11:11AM",
							"end_time": "Mar 1 2020 2:00PM"
						},
						{
							"start_time": "Mar 16 2020  5:33PM",
							"end_time": "Mar 16 2020 8:02PM"
						}
					]
				},
				{
					"id": "W07QCRPA4",
					"real_name": "Glinda Southgood",
					"tz": "Asia/Kolkata",
					"activity_periods": [{
							"start_time": "Feb 1 2020  1:33PM",
							"end_time": "Feb 1 2020 1:54PM"
						},
						{
							"start_time": "Mar 1 2020  11:11AM",
							"end_time": "Mar 1 2020 2:00PM"
						},
						{
							"start_time": "Mar 16 2020  5:33PM",
							"end_time": "Mar 16 2020 8:02PM"
						}
					]
				}
			]
		}
