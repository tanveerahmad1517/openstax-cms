import ast
from django.core.management.base import BaseCommand
from salesforce.models import School, MapBoxDataset
from mapbox import Datasets
from django.conf import settings


class Command(BaseCommand):
    help = "upload geoJSON school data to Mapbox"

    def handle(self, *args, **options):
        datasets = Datasets(access_token=settings.MAPBOX_TOKEN)
        try:
            mapbox_dataset = MapBoxDataset.objects.all()[0] #check if a dataset was already created
            dataset_id = mapbox_dataset.dataset_id
            dataset = datasets.read_dataset(dataset_id).json()
        except IndexError: #it wasn't, let's do that
            dataset = datasets.create(name='os-schools', description='A listing of OpenStax Adoptions')
            dataset_decoded = ast.literal_eval(dataset.content.decode())

            mapbox_dataset_created, _ = MapBoxDataset.objects.get_or_create(name=dataset_decoded["name"],
                                                                            dataset_id=dataset_decoded["id"])
            dataset_id = mapbox_dataset_created.dataset_id


        #cool - we have a dataset, now let's fill it with school location data
        schools = School.objects.all()

        for school in schools:
            feature = {
                'type': 'Feature',
                'geometry': {
                    'type': "Point",
                    'coordinates': [float(school.long), float(school.lat)]
                },
                'properties': {
                    'name': school.name
                }
            }
            datasets.update_feature(dataset_id, school.pk, feature)


        self.stdout.write("fin")
