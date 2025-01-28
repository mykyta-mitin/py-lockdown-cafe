import datetime
from app.cafe import Cafe
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    try:
        friends_without_mask = 0

        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotVaccinatedError:
                return "All friends should be vaccinated"
            except OutdatedVaccineError:
                return "All friends should be vaccinated"
            except NotWearingMaskError:
                friends_without_mask += 1

        if friends_without_mask > 0:
                return f"Friends should buy {friends_without_mask} masks"

        return f"Friends can go to {cafe.name}"

    except Exception as e:
        print(f"Unexpected error: {e}")
