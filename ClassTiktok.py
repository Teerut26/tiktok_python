# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = ClassTiktokfromdict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, Callable, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Author:
    id: Optional[str] = None
    uniqueId: Optional[str] = None
    nickname: Optional[str] = None
    avatarThumb: Optional[str] = None
    avatarMedium: Optional[str] = None
    avatarLarger: Optional[str] = None
    signature: Optional[str] = None
    verified: Optional[bool] = None
    secUid: Optional[str] = None
    secret: Optional[bool] = None
    ftc: Optional[bool] = None
    relation: Optional[int] = None
    openFavorite: Optional[bool] = None
    commentSetting: Optional[int] = None
    duetSetting: Optional[int] = None
    stitchSetting: Optional[int] = None
    privateAccount: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Author':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        uniqueId = from_union([from_str, from_none], obj.get("uniqueId"))
        nickname = from_union([from_str, from_none], obj.get("nickname"))
        avatarThumb = from_union([from_str, from_none], obj.get("avatarThumb"))
        avatarMedium = from_union([from_str, from_none], obj.get("avatarMedium"))
        avatarLarger = from_union([from_str, from_none], obj.get("avatarLarger"))
        signature = from_union([from_str, from_none], obj.get("signature"))
        verified = from_union([from_bool, from_none], obj.get("verified"))
        secUid = from_union([from_str, from_none], obj.get("secUid"))
        secret = from_union([from_bool, from_none], obj.get("secret"))
        ftc = from_union([from_bool, from_none], obj.get("ftc"))
        relation = from_union([from_int, from_none], obj.get("relation"))
        openFavorite = from_union([from_bool, from_none], obj.get("openFavorite"))
        commentSetting = from_union([from_int, from_none], obj.get("commentSetting"))
        duetSetting = from_union([from_int, from_none], obj.get("duetSetting"))
        stitchSetting = from_union([from_int, from_none], obj.get("stitchSetting"))
        privateAccount = from_union([from_bool, from_none], obj.get("privateAccount"))
        return Author(id, uniqueId, nickname, avatarThumb, avatarMedium, avatarLarger, signature, verified, secUid, secret, ftc, relation, openFavorite, commentSetting, duetSetting, stitchSetting, privateAccount)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["uniqueId"] = from_union([from_str, from_none], self.uniqueId)
        result["nickname"] = from_union([from_str, from_none], self.nickname)
        result["avatarThumb"] = from_union([from_str, from_none], self.avatarThumb)
        result["avatarMedium"] = from_union([from_str, from_none], self.avatarMedium)
        result["avatarLarger"] = from_union([from_str, from_none], self.avatarLarger)
        result["signature"] = from_union([from_str, from_none], self.signature)
        result["verified"] = from_union([from_bool, from_none], self.verified)
        result["secUid"] = from_union([from_str, from_none], self.secUid)
        result["secret"] = from_union([from_bool, from_none], self.secret)
        result["ftc"] = from_union([from_bool, from_none], self.ftc)
        result["relation"] = from_union([from_int, from_none], self.relation)
        result["openFavorite"] = from_union([from_bool, from_none], self.openFavorite)
        result["commentSetting"] = from_union([from_int, from_none], self.commentSetting)
        result["duetSetting"] = from_union([from_int, from_none], self.duetSetting)
        result["stitchSetting"] = from_union([from_int, from_none], self.stitchSetting)
        result["privateAccount"] = from_union([from_bool, from_none], self.privateAccount)
        return result


@dataclass
class AuthorStats:
    followingCount: Optional[int] = None
    followerCount: Optional[int] = None
    heartCount: Optional[int] = None
    videoCount: Optional[int] = None
    diggCount: Optional[int] = None
    heart: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AuthorStats':
        assert isinstance(obj, dict)
        followingCount = from_union([from_int, from_none], obj.get("followingCount"))
        followerCount = from_union([from_int, from_none], obj.get("followerCount"))
        heartCount = from_union([from_int, from_none], obj.get("heartCount"))
        videoCount = from_union([from_int, from_none], obj.get("videoCount"))
        diggCount = from_union([from_int, from_none], obj.get("diggCount"))
        heart = from_union([from_int, from_none], obj.get("heart"))
        return AuthorStats(followingCount, followerCount, heartCount, videoCount, diggCount, heart)

    def to_dict(self) -> dict:
        result: dict = {}
        result["followingCount"] = from_union([from_int, from_none], self.followingCount)
        result["followerCount"] = from_union([from_int, from_none], self.followerCount)
        result["heartCount"] = from_union([from_int, from_none], self.heartCount)
        result["videoCount"] = from_union([from_int, from_none], self.videoCount)
        result["diggCount"] = from_union([from_int, from_none], self.diggCount)
        result["heart"] = from_union([from_int, from_none], self.heart)
        return result


@dataclass
class Challenge:
    id: Optional[str] = None
    title: Optional[str] = None
    desc: Optional[str] = None
    profileThumb: Optional[str] = None
    profileMedium: Optional[str] = None
    profileLarger: Optional[str] = None
    coverThumb: Optional[str] = None
    coverMedium: Optional[str] = None
    coverLarger: Optional[str] = None
    isCommerce: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Challenge':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        desc = from_union([from_str, from_none], obj.get("desc"))
        profileThumb = from_union([from_str, from_none], obj.get("profileThumb"))
        profileMedium = from_union([from_str, from_none], obj.get("profileMedium"))
        profileLarger = from_union([from_str, from_none], obj.get("profileLarger"))
        coverThumb = from_union([from_str, from_none], obj.get("coverThumb"))
        coverMedium = from_union([from_str, from_none], obj.get("coverMedium"))
        coverLarger = from_union([from_str, from_none], obj.get("coverLarger"))
        isCommerce = from_union([from_bool, from_none], obj.get("isCommerce"))
        return Challenge(id, title, desc, profileThumb, profileMedium, profileLarger, coverThumb, coverMedium, coverLarger, isCommerce)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["desc"] = from_union([from_str, from_none], self.desc)
        result["profileThumb"] = from_union([from_str, from_none], self.profileThumb)
        result["profileMedium"] = from_union([from_str, from_none], self.profileMedium)
        result["profileLarger"] = from_union([from_str, from_none], self.profileLarger)
        result["coverThumb"] = from_union([from_str, from_none], self.coverThumb)
        result["coverMedium"] = from_union([from_str, from_none], self.coverMedium)
        result["coverLarger"] = from_union([from_str, from_none], self.coverLarger)
        result["isCommerce"] = from_union([from_bool, from_none], self.isCommerce)
        return result


@dataclass
class DuetInfo:
    duetFromId: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DuetInfo':
        assert isinstance(obj, dict)
        duetFromId = from_union([from_none, lambda x: int(from_str(x))], obj.get("duetFromId"))
        return DuetInfo(duetFromId)

    def to_dict(self) -> dict:
        result: dict = {}
        result["duetFromId"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.duetFromId)
        return result


class Album(Enum):
    AstronautInTheOcean = "Astronaut In The Ocean"
    empty = ""


@dataclass
class Music:
    id: Optional[str] = None
    title: Optional[str] = None
    playUrl: Optional[str] = None
    coverThumb: Optional[str] = None
    coverMedium: Optional[str] = None
    coverLarge: Optional[str] = None
    authorName: Optional[str] = None
    original: Optional[bool] = None
    duration: Optional[int] = None
    album: Optional[Album] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Music':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        playUrl = from_union([from_str, from_none], obj.get("playUrl"))
        coverThumb = from_union([from_str, from_none], obj.get("coverThumb"))
        coverMedium = from_union([from_str, from_none], obj.get("coverMedium"))
        coverLarge = from_union([from_str, from_none], obj.get("coverLarge"))
        authorName = from_union([from_str, from_none], obj.get("authorName"))
        original = from_union([from_bool, from_none], obj.get("original"))
        duration = from_union([from_int, from_none], obj.get("duration"))
        album = from_union([Album, from_none], obj.get("album"))
        return Music(id, title, playUrl, coverThumb, coverMedium, coverLarge, authorName, original, duration, album)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["playUrl"] = from_union([from_str, from_none], self.playUrl)
        result["coverThumb"] = from_union([from_str, from_none], self.coverThumb)
        result["coverMedium"] = from_union([from_str, from_none], self.coverMedium)
        result["coverLarge"] = from_union([from_str, from_none], self.coverLarge)
        result["authorName"] = from_union([from_str, from_none], self.authorName)
        result["original"] = from_union([from_bool, from_none], self.original)
        result["duration"] = from_union([from_int, from_none], self.duration)
        result["album"] = from_union([lambda x: to_enum(Album, x), from_none], self.album)
        return result


@dataclass
class Stats:
    diggCount: Optional[int] = None
    shareCount: Optional[int] = None
    commentCount: Optional[int] = None
    playCount: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Stats':
        assert isinstance(obj, dict)
        diggCount = from_union([from_int, from_none], obj.get("diggCount"))
        shareCount = from_union([from_int, from_none], obj.get("shareCount"))
        commentCount = from_union([from_int, from_none], obj.get("commentCount"))
        playCount = from_union([from_int, from_none], obj.get("playCount"))
        return Stats(diggCount, shareCount, commentCount, playCount)

    def to_dict(self) -> dict:
        result: dict = {}
        result["diggCount"] = from_union([from_int, from_none], self.diggCount)
        result["shareCount"] = from_union([from_int, from_none], self.shareCount)
        result["commentCount"] = from_union([from_int, from_none], self.commentCount)
        result["playCount"] = from_union([from_int, from_none], self.playCount)
        return result


@dataclass
class StickersOnItem:
    stickerType: Optional[int] = None
    stickerText: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StickersOnItem':
        assert isinstance(obj, dict)
        stickerType = from_union([from_int, from_none], obj.get("stickerType"))
        stickerText = from_union([lambda x: from_list(from_str, x), from_none], obj.get("stickerText"))
        return StickersOnItem(stickerType, stickerText)

    def to_dict(self) -> dict:
        result: dict = {}
        result["stickerType"] = from_union([from_int, from_none], self.stickerType)
        result["stickerText"] = from_union([lambda x: from_list(from_str, x), from_none], self.stickerText)
        return result


@dataclass
class TextExtra:
    awemeId: Optional[str] = None
    start: Optional[int] = None
    end: Optional[int] = None
    hashtagName: Optional[str] = None
    hashtagId: Optional[str] = None
    type: Optional[int] = None
    userId: Optional[str] = None
    isCommerce: Optional[bool] = None
    userUniqueId: Optional[str] = None
    secUid: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TextExtra':
        assert isinstance(obj, dict)
        awemeId = from_union([from_str, from_none], obj.get("awemeId"))
        start = from_union([from_int, from_none], obj.get("start"))
        end = from_union([from_int, from_none], obj.get("end"))
        hashtagName = from_union([from_str, from_none], obj.get("hashtagName"))
        hashtagId = from_union([from_str, from_none], obj.get("hashtagId"))
        type = from_union([from_int, from_none], obj.get("type"))
        userId = from_union([from_str, from_none], obj.get("userId"))
        isCommerce = from_union([from_bool, from_none], obj.get("isCommerce"))
        userUniqueId = from_union([from_str, from_none], obj.get("userUniqueId"))
        secUid = from_union([from_str, from_none], obj.get("secUid"))
        return TextExtra(awemeId, start, end, hashtagName, hashtagId, type, userId, isCommerce, userUniqueId, secUid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["awemeId"] = from_union([from_str, from_none], self.awemeId)
        result["start"] = from_union([from_int, from_none], self.start)
        result["end"] = from_union([from_int, from_none], self.end)
        result["hashtagName"] = from_union([from_str, from_none], self.hashtagName)
        result["hashtagId"] = from_union([from_str, from_none], self.hashtagId)
        result["type"] = from_union([from_int, from_none], self.type)
        result["userId"] = from_union([from_str, from_none], self.userId)
        result["isCommerce"] = from_union([from_bool, from_none], self.isCommerce)
        result["userUniqueId"] = from_union([from_str, from_none], self.userUniqueId)
        result["secUid"] = from_union([from_str, from_none], self.secUid)
        return result


class CodecType(Enum):
    h264 = "h264"


class Definition(Enum):
    the720p = "720p"


class EncodedType(Enum):
    normal = "normal"


class Format(Enum):
    mp4 = "mp4"


@dataclass
class Video:
    id: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None
    duration: Optional[int] = None
    ratio: Optional[Definition] = None
    cover: Optional[str] = None
    originCover: Optional[str] = None
    dynamicCover: Optional[str] = None
    playAddr: Optional[str] = None
    downloadAddr: Optional[str] = None
    shareCover: Optional[List[str]] = None
    reflowCover: Optional[str] = None
    bitrate: Optional[int] = None
    encodedType: Optional[EncodedType] = None
    format: Optional[Format] = None
    videoQuality: Optional[EncodedType] = None
    encodeUserTag: Optional[str] = None
    codecType: Optional[CodecType] = None
    definition: Optional[Definition] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Video':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        height = from_union([from_int, from_none], obj.get("height"))
        width = from_union([from_int, from_none], obj.get("width"))
        duration = from_union([from_int, from_none], obj.get("duration"))
        ratio = from_union([Definition, from_none], obj.get("ratio"))
        cover = from_union([from_str, from_none], obj.get("cover"))
        originCover = from_union([from_str, from_none], obj.get("originCover"))
        dynamicCover = from_union([from_str, from_none], obj.get("dynamicCover"))
        playAddr = from_union([from_str, from_none], obj.get("playAddr"))
        downloadAddr = from_union([from_str, from_none], obj.get("downloadAddr"))
        shareCover = from_union([lambda x: from_list(from_str, x), from_none], obj.get("shareCover"))
        reflowCover = from_union([from_str, from_none], obj.get("reflowCover"))
        bitrate = from_union([from_int, from_none], obj.get("bitrate"))
        encodedType = from_union([EncodedType, from_none], obj.get("encodedType"))
        format = from_union([Format, from_none], obj.get("format"))
        videoQuality = from_union([EncodedType, from_none], obj.get("videoQuality"))
        encodeUserTag = from_union([from_str, from_none], obj.get("encodeUserTag"))
        codecType = from_union([CodecType, from_none], obj.get("codecType"))
        definition = from_union([Definition, from_none], obj.get("definition"))
        return Video(id, height, width, duration, ratio, cover, originCover, dynamicCover, playAddr, downloadAddr, shareCover, reflowCover, bitrate, encodedType, format, videoQuality, encodeUserTag, codecType, definition)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["height"] = from_union([from_int, from_none], self.height)
        result["width"] = from_union([from_int, from_none], self.width)
        result["duration"] = from_union([from_int, from_none], self.duration)
        result["ratio"] = from_union([lambda x: to_enum(Definition, x), from_none], self.ratio)
        result["cover"] = from_union([from_str, from_none], self.cover)
        result["originCover"] = from_union([from_str, from_none], self.originCover)
        result["dynamicCover"] = from_union([from_str, from_none], self.dynamicCover)
        result["playAddr"] = from_union([from_str, from_none], self.playAddr)
        result["downloadAddr"] = from_union([from_str, from_none], self.downloadAddr)
        result["shareCover"] = from_union([lambda x: from_list(from_str, x), from_none], self.shareCover)
        result["reflowCover"] = from_union([from_str, from_none], self.reflowCover)
        result["bitrate"] = from_union([from_int, from_none], self.bitrate)
        result["encodedType"] = from_union([lambda x: to_enum(EncodedType, x), from_none], self.encodedType)
        result["format"] = from_union([lambda x: to_enum(Format, x), from_none], self.format)
        result["videoQuality"] = from_union([lambda x: to_enum(EncodedType, x), from_none], self.videoQuality)
        result["encodeUserTag"] = from_union([from_str, from_none], self.encodeUserTag)
        result["codecType"] = from_union([lambda x: to_enum(CodecType, x), from_none], self.codecType)
        result["definition"] = from_union([lambda x: to_enum(Definition, x), from_none], self.definition)
        return result


@dataclass
class ClassTiktokElement:
    id: Optional[str] = None
    desc: Optional[str] = None
    createTime: Optional[int] = None
    video: Optional[Video] = None
    author: Optional[Author] = None
    music: Optional[Music] = None
    stats: Optional[Stats] = None
    duetInfo: Optional[DuetInfo] = None
    originalItem: Optional[bool] = None
    officalItem: Optional[bool] = None
    secret: Optional[bool] = None
    forFriend: Optional[bool] = None
    digged: Optional[bool] = None
    itemCommentStatus: Optional[int] = None
    showNotPass: Optional[bool] = None
    vl1: Optional[bool] = None
    itemMute: Optional[bool] = None
    authorStats: Optional[AuthorStats] = None
    privateItem: Optional[bool] = None
    duetEnabled: Optional[bool] = None
    stitchEnabled: Optional[bool] = None
    shareEnabled: Optional[bool] = None
    isAd: Optional[bool] = None
    duetDisplay: Optional[int] = None
    stitchDisplay: Optional[int] = None
    challenges: Optional[List[Challenge]] = None
    textExtra: Optional[List[TextExtra]] = None
    stickersOnItem: Optional[List[StickersOnItem]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ClassTiktokElement':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        desc = from_union([from_str, from_none], obj.get("desc"))
        createTime = from_union([from_int, from_none], obj.get("createTime"))
        video = from_union([Video.from_dict, from_none], obj.get("video"))
        author = from_union([Author.from_dict, from_none], obj.get("author"))
        music = from_union([Music.from_dict, from_none], obj.get("music"))
        stats = from_union([Stats.from_dict, from_none], obj.get("stats"))
        duetInfo = from_union([DuetInfo.from_dict, from_none], obj.get("duetInfo"))
        originalItem = from_union([from_bool, from_none], obj.get("originalItem"))
        officalItem = from_union([from_bool, from_none], obj.get("officalItem"))
        secret = from_union([from_bool, from_none], obj.get("secret"))
        forFriend = from_union([from_bool, from_none], obj.get("forFriend"))
        digged = from_union([from_bool, from_none], obj.get("digged"))
        itemCommentStatus = from_union([from_int, from_none], obj.get("itemCommentStatus"))
        showNotPass = from_union([from_bool, from_none], obj.get("showNotPass"))
        vl1 = from_union([from_bool, from_none], obj.get("vl1"))
        itemMute = from_union([from_bool, from_none], obj.get("itemMute"))
        authorStats = from_union([AuthorStats.from_dict, from_none], obj.get("authorStats"))
        privateItem = from_union([from_bool, from_none], obj.get("privateItem"))
        duetEnabled = from_union([from_bool, from_none], obj.get("duetEnabled"))
        stitchEnabled = from_union([from_bool, from_none], obj.get("stitchEnabled"))
        shareEnabled = from_union([from_bool, from_none], obj.get("shareEnabled"))
        isAd = from_union([from_bool, from_none], obj.get("isAd"))
        duetDisplay = from_union([from_int, from_none], obj.get("duetDisplay"))
        stitchDisplay = from_union([from_int, from_none], obj.get("stitchDisplay"))
        challenges = from_union([lambda x: from_list(Challenge.from_dict, x), from_none], obj.get("challenges"))
        textExtra = from_union([lambda x: from_list(TextExtra.from_dict, x), from_none], obj.get("textExtra"))
        stickersOnItem = from_union([lambda x: from_list(StickersOnItem.from_dict, x), from_none], obj.get("stickersOnItem"))
        return ClassTiktokElement(id, desc, createTime, video, author, music, stats, duetInfo, originalItem, officalItem, secret, forFriend, digged, itemCommentStatus, showNotPass, vl1, itemMute, authorStats, privateItem, duetEnabled, stitchEnabled, shareEnabled, isAd, duetDisplay, stitchDisplay, challenges, textExtra, stickersOnItem)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["desc"] = from_union([from_str, from_none], self.desc)
        result["createTime"] = from_union([from_int, from_none], self.createTime)
        result["video"] = from_union([lambda x: to_class(Video, x), from_none], self.video)
        result["author"] = from_union([lambda x: to_class(Author, x), from_none], self.author)
        result["music"] = from_union([lambda x: to_class(Music, x), from_none], self.music)
        result["stats"] = from_union([lambda x: to_class(Stats, x), from_none], self.stats)
        result["duetInfo"] = from_union([lambda x: to_class(DuetInfo, x), from_none], self.duetInfo)
        result["originalItem"] = from_union([from_bool, from_none], self.originalItem)
        result["officalItem"] = from_union([from_bool, from_none], self.officalItem)
        result["secret"] = from_union([from_bool, from_none], self.secret)
        result["forFriend"] = from_union([from_bool, from_none], self.forFriend)
        result["digged"] = from_union([from_bool, from_none], self.digged)
        result["itemCommentStatus"] = from_union([from_int, from_none], self.itemCommentStatus)
        result["showNotPass"] = from_union([from_bool, from_none], self.showNotPass)
        result["vl1"] = from_union([from_bool, from_none], self.vl1)
        result["itemMute"] = from_union([from_bool, from_none], self.itemMute)
        result["authorStats"] = from_union([lambda x: to_class(AuthorStats, x), from_none], self.authorStats)
        result["privateItem"] = from_union([from_bool, from_none], self.privateItem)
        result["duetEnabled"] = from_union([from_bool, from_none], self.duetEnabled)
        result["stitchEnabled"] = from_union([from_bool, from_none], self.stitchEnabled)
        result["shareEnabled"] = from_union([from_bool, from_none], self.shareEnabled)
        result["isAd"] = from_union([from_bool, from_none], self.isAd)
        result["duetDisplay"] = from_union([from_int, from_none], self.duetDisplay)
        result["stitchDisplay"] = from_union([from_int, from_none], self.stitchDisplay)
        result["challenges"] = from_union([lambda x: from_list(lambda x: to_class(Challenge, x), x), from_none], self.challenges)
        result["textExtra"] = from_union([lambda x: from_list(lambda x: to_class(TextExtra, x), x), from_none], self.textExtra)
        result["stickersOnItem"] = from_union([lambda x: from_list(lambda x: to_class(StickersOnItem, x), x), from_none], self.stickersOnItem)
        return result


def ClassTiktokfromdict(s: Any) -> List[ClassTiktokElement]:
    return from_list(ClassTiktokElement.from_dict, s)


def ClassTiktoktodict(x: List[ClassTiktokElement]) -> Any:
    return from_list(lambda x: to_class(ClassTiktokElement, x), x)
