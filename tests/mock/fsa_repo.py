
from goald.config.utils.repository_builder import RepositoryBuilder
from goald.config.model.ve import VE
from goald.config.planning.dvm_builder import DVMBuilder
from goald.config.repo.hash_map_repository import HashMapRepository


def fsa_dvm() -> VE:
    repo = fsa_repo()
    return DVMBuilder(repo).resolveRootGoal('displayMyPosition')


def fsa_repo() -> HashMapRepository:
    return RepositoryBuilder() \
        .withMetadata('defines', 'provides','conditions',
                      'quality', 'dependsOnAny', 'dependsOnCond') \
        .withBundle(
            'greater.def',
            defines=['greet']) \
        .withBundle(
            'greater.impl',
            provides=['greet'],
            conditions=['display_capability']) \
        .withBundle(
            'alarm.def',
            defines=['alarm']) \
        .withBundle(
            'alarm',
            provides=['alarm'],
            conditions=['sound_capability']) \
        .withBundle(
            'displayORAlert.def',
            defines=['displayORAlert']) \
        .withBundle(
            'displayORAlert.impl',
            provides=['displayORAlert'],
            dependsOnAny=['displayMyPosition', 'alarm']) \
        .withBundle(
            'displayMyPosition.def',
            defines=['displayMyPosition']) \
        .withBundle(
            'displayMyPosition.impl',
            provides=['displayMyPosition'],
            dependsOn=['getPosition', 'mapView']) \
        .withBundle(
            'getPosition.def',
            defines='getPosition') \
        .withBundle(
            'getPositionByGPS',
            provides=['getPosition'],
            conditions=['gps_capability'],
            quality=[('precision', 10), ('responseTime', 5)]) \
        .withBundle(
            'getPositionByAntenna',
            provides=['getPosition'],
            conditions=['antenna_capability'],
            quality=[('precision', 5), ('responseTime', 10)]) \
        .withBundle(
            'mapView.def',
            defines=['mapView']) \
        .withBundle(
            'mapView.impl',
            provides=['mapView'],
            conditions=['display_capability']) \
        .withBundle(
            'timeManager.def',
            defines=['timeManager']) \
        .withBundle(
            'timeManager.impl',
            provides=['timeManager'],
            dependsOnAny=['alarm']) \
        .withBundle(
            'premiumDriveTips.def',
            defines=['premiumDriveTips']) \
        .withBundle(
            'premiumDriveTips.impl',
            provides=['premiumDriveTips'],
            dependsOnCond=['nearby', 'mapView']) \
        .withBundle(
            'soundAlertWhileDriving.def',
            defines=['soundAlertWhileDriving']) \
        .withBundle(
            'soundAlertWhileDriving.impl',
            provides=['soundAlertWhileDriving'],
            dependsOnCond=[('gps_capability', 'displayMyPosition'),
                           ('sound_alert_active', 'alarm')]) \
        .create()
