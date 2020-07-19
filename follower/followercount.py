from core.timemapdownloader import TimeMapDownloader
from core.mementodownloader import MementoDownloader
from follower.followeranalysis import FollowerAnalysis


class FollowerCount:
    def __init__(self, thandle, conf_reader, constants, dmanager, logger):
        self.__thandle = thandle
        self.__conf_reader = conf_reader
        self.__constants = constants
        self.__dmanager = dmanager
        self.__logger = logger

    def get_follower_count(self):
        turl = self.__constants.TWITTER_URL + self.__thandle
        self.__logger.access_log.debug("Start: (main)" + turl)
        tm_object = TimeMapDownloader(self.__thandle, self.__constants, self.__dmanager, self.__logger)
        tm_status = tm_object.fetch_timemap(turl)
        self.__logger.access_log.debug("Start: (main): Fetching timemap done: " + turl)
        if tm_status:
            mobject = MementoDownloader(self.__thandle, turl, self.__constants, self.__dmanager, self.__logger)
            mobject.get_memento(self.__conf_reader)
            self.__logger.access_log.debug("Start: (main): Fetching mementos, Parsing mementos and filling them in "
                                           "database done done: ")

    def get_follower_analysis(self):
        fanalysis = FollowerAnalysis(self.__thandle, self.__conf_reader, self.__constants, self.__dmanager,
                                     self.__logger)
        fanalysis.relative_analysis()