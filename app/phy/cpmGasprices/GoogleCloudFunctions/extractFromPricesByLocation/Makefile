#https://cloud.google.com/functions/docs/calling/storage#functions-calling-storage-python
#
#gcloud functions deploy hello_gcs \
#--runtime python39 \
#--trigger-resource YOUR_TRIGGER_BUCKET_NAME \
#--trigger-event google.storage.object.finalize

deploy:
	gcloud functions deploy visualize_weekly_http --runtime=python39 --trigger-http --allow-unauthenticated --region=europe-west3 --memory=256MB
	gcloud functions deploy visualize_weekly --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=256MB --retry
	gcloud functions deploy extract_from_prices_by_location --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=1024MB --retry
	gcloud functions deploy concat_price_stations_21days_timespans --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=256MB --retry


concat_price_stations_21days_timespans_deploy:
	gcloud functions deploy concat_price_stations_21days_timespans --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=256MB --retry

visualize_weekly_deploy:
	gcloud functions deploy visualize_weekly --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=256MB --retry