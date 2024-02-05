from nepali_date_utils.data import calendar_data
from datetime import datetime, timedelta


class DateConverter:
    en_max_year = 2099
    en_min_year = 1944
    days_in_year = 365
    reference_ad = {"year": 2017, "month": 2, "day": 11}
    reference_bs = {"year": 2073, "month": 10, "day": 29}

    def verify_nepali_date(self, date_obj):
        year = date_obj["year"]
        month = date_obj["month"]
        day = date_obj["day"]
        return (
            self.en_min_year <= year <= self.en_max_year
            and 1 <= month <= 12
            and 1 <= day <= 31
        )

    def difference_in_ad(self, date):
        # Split the date string into year, month, and day components
        date_arr = list(map(int, date.split("/")))

        # Create a dictionary to represent the date object
        date_obj = {"year": date_arr[0], "month": date_arr[1], "day": date_arr[2]}

        # Create datetime objects for the base date and the input date
        date1 = datetime(
            self.reference_ad["year"],
            self.reference_ad["month"],
            self.reference_ad["day"],
        )
        date2 = datetime(date_obj["year"], date_obj["month"], date_obj["day"])

        # Calculate the difference in days
        time_diff = date2 - date1
        diff_days = time_diff.days

        return {"diff_days": diff_days}

    def convert_to_bs(self, day_data):
        try:
            day_count = day_data["diff_days"]
            bs_date = self.reference_bs.copy()
            if day_count >= 0:
                bs_date["day"] += day_count
                while (
                    bs_date["day"]
                    > calendar_data[bs_date["year"]][bs_date["month"] - 1]
                ):
                    bs_date["day"] -= calendar_data[bs_date["year"]][
                        bs_date["month"] - 1
                    ]
                    bs_date["month"] += 1
                    if bs_date["month"] > 12:
                        bs_date["year"] += 1
                        bs_date["month"] = 1
            else:
                day_count = abs(day_count)
                while day_count >= 0:
                    if day_count < calendar_data[bs_date["year"]][bs_date["month"] - 1]:
                        day_count = (
                            calendar_data[bs_date["year"]][bs_date["month"] - 1]
                            - day_count
                        )
                        break
                    day_count -= calendar_data[bs_date["year"]][bs_date["month"] - 1]
                    bs_date["month"] -= 1
                    if bs_date["month"] == 0:
                        bs_date["year"] -= 1
                        bs_date["month"] = 12
                bs_date["day"] = day_count
            return bs_date
        except KeyError:
            raise ValueError("Date out of range")

    def difference_in_bs(self, date):
        date_arr = list(map(int, date.split("/")))
        date_obj = {"year": date_arr[0], "month": date_arr[1], "day": date_arr[2]}

        start, end = (
            (self.reference_bs, date_obj)
            if (date_obj["year"], date_obj["month"], date_obj["day"])
            > (
                self.reference_bs["year"],
                self.reference_bs["month"],
                self.reference_bs["day"],
            )
            else (date_obj, self.reference_bs)
        )
        factor = (
            1
            if (date_obj["year"], date_obj["month"], date_obj["day"])
            > (
                self.reference_bs["year"],
                self.reference_bs["month"],
                self.reference_bs["day"],
            )
            else -1
        )

        day_count = sum(
            calendar_data[i][12] for i in range(start["year"], end["year"] + 1)
        )
        day_count -= sum(
            calendar_data[start["year"]][i] for i in range(start["month"] - 1)
        )
        day_count -= sum(
            calendar_data[end["year"]][i] for i in range(end["month"] - 1, 12)
        )
        day_count -= start["day"]
        day_count += end["day"]

        return day_count * factor

    def offset_ad_days(self, day_count):
        base_date = datetime(
            self.reference_ad["year"],
            self.reference_ad["month"],
            self.reference_ad["day"],
        )
        offset_date = base_date + timedelta(days=day_count)

        month = offset_date.month

        date_obj = {"year": offset_date.year, "month": month, "day": offset_date.day}

        return date_obj

    @classmethod
    def ad_to_bs(cls, date_str):
        return cls().convert_to_bs(cls().difference_in_ad(date_str))

    @staticmethod
    def parse_date(date_str):
        date_arr = list(map(int, date_str.split("/")))
        return {"year": date_arr[0], "month": date_arr[1], "day": date_arr[2]}

    @classmethod
    def bs_to_ad(cls, date_str):
        date_obj = cls().parse_date(date_str)
        if not converter.verify_nepali_date(
            date_obj
        ):  # Call verify_nepali_date on the instance
            raise ValueError("Date out of range")
        difference = converter.difference_in_bs(
            date_str
        )  # Call difference_in_bs on the instance
        return converter.offset_ad_days(
            difference
        )  # Call offset_ad_days on the instance


converter = DateConverter()
