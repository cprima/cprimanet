#https://cloud.google.com/functions/docs/calling/storage#functions-calling-storage-python

deploy:
	cd src; gcloud functions deploy download_pricefiles_http --runtime=python39 --trigger-http --allow-unauthenticated --region=europe-west3 --memory=256MB
	cd src; gcloud functions deploy download_pricefiles --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=256MB --retry
	cd src; gcloud functions deploy download_stationsfiles --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=256MB --retry
	@#
	cd src; gcloud functions deploy extract_from_pricefile_for_location_http --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=1024MB --retry
	cd src; gcloud functions deploy extract_from_pricefile_for_location --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=1024MB --retry
	@#
	cd src; gcloud functions deploy merge_stationprices_http --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=256MB --retry
	cd src; gcloud functions deploy merge_stationprices --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=256MB --retry
	@#
	@#cd src; gcloud functions deploy visualize_weekly_http --runtime=python39 --trigger-http --allow-unauthenticated --region=europe-west3 --memory=256MB
	@#cd src; gcloud functions deploy visualize_weekly --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=256MB --retry
	@#cd src; gcloud functions deploy extract_from_prices_by_location --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=1024MB --retry
	@#cd src; gcloud functions deploy concat_price_stations_21days_timespans --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=256MB --retry


concat_price_stations_21days_timespans_deploy:
	cd src; gcloud functions deploy concat_price_stations_21days_timespans --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=256MB --retry

visualize_weekly_deploy:
	cd src; gcloud functions deploy visualize_weekly_http --runtime=python39 --trigger-http --allow-unauthenticated --region=europe-west3 --memory=256MB
	cd src; gcloud functions deploy visualize_weekly --runtime=python39 --trigger-resource=2021.gasprices.cprima.net --trigger-event=google.storage.object.finalize --region=europe-west3 --memory=256MB --retry