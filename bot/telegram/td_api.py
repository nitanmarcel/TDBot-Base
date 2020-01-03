from __future__ import annotations

import decimal
import typing
import json
import inspect

import attr


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class RootObject:
    __tdlib_type__ = "RootObject"
    _extra: str = attr.ib(default="", repr=False, cmp=False)

    def __init__(self):
        pass

    def stringify(self):
        return self._stringify(self)

    def _stringify(self, obj, indent=0):
        result = []
        obj_type = getattr(obj, '__tdlib_type__', '_')
        if isinstance(obj, type) and obj.__name__ == '_empty':
            obj = None
        if hasattr(obj, '__dict__'):
            obj = obj.__dict__
        if isinstance(obj, dict):
            result.append(obj_type)
            result.append('(')
            if obj:
                result.append('\n')
                indent += 1
                for k_, v_ in obj.items():
                    result.append('\t' * indent)
                    result.append(k_)
                    result.append('=')
                    result.append(self._stringify(v_, 1))
                    result.append(',\n')
                result.pop()
                indent -= 1
                result.append('\n')
                result.append('\t' * indent)
            result.append(')')
        else:
            return repr(obj)

        return ' '.join(result)

    def to_dict(self):
        return self.__dict__


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class AccountTtl(RootObject):
    __tdlib_type__ = "AccountTtl"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Address(RootObject):
    __tdlib_type__ = "Address"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Animation(RootObject):
    __tdlib_type__ = "Animation"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Animations(RootObject):
    __tdlib_type__ = "Animations"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Audio(RootObject):
    __tdlib_type__ = "Audio"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class AuthenticationCodeInfo(RootObject):
    __tdlib_type__ = "AuthenticationCodeInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class AuthenticationCodeType(RootObject):
    __tdlib_type__ = "AuthenticationCodeType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class AuthorizationState(RootObject):
    __tdlib_type__ = "AuthorizationState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class AutoDownloadSettings(RootObject):
    __tdlib_type__ = "AutoDownloadSettings"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class AutoDownloadSettingsPresets(RootObject):
    __tdlib_type__ = "AutoDownloadSettingsPresets"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Background(RootObject):
    __tdlib_type__ = "Background"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class BackgroundFill(RootObject):
    __tdlib_type__ = "BackgroundFill"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class BackgroundType(RootObject):
    __tdlib_type__ = "BackgroundType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Backgrounds(RootObject):
    __tdlib_type__ = "Backgrounds"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class BasicGroup(RootObject):
    __tdlib_type__ = "BasicGroup"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class BasicGroupFullInfo(RootObject):
    __tdlib_type__ = "BasicGroupFullInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class BotCommand(RootObject):
    __tdlib_type__ = "BotCommand"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class BotInfo(RootObject):
    __tdlib_type__ = "BotInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Call(RootObject):
    __tdlib_type__ = "Call"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class CallConnection(RootObject):
    __tdlib_type__ = "CallConnection"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class CallDiscardReason(RootObject):
    __tdlib_type__ = "CallDiscardReason"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class CallId(RootObject):
    __tdlib_type__ = "CallId"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class CallProblem(RootObject):
    __tdlib_type__ = "CallProblem"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class CallProtocol(RootObject):
    __tdlib_type__ = "CallProtocol"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class CallState(RootObject):
    __tdlib_type__ = "CallState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class CallbackQueryAnswer(RootObject):
    __tdlib_type__ = "CallbackQueryAnswer"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class CallbackQueryPayload(RootObject):
    __tdlib_type__ = "CallbackQueryPayload"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class CanTransferOwnershipResult(RootObject):
    __tdlib_type__ = "CanTransferOwnershipResult"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Chat(RootObject):
    __tdlib_type__ = "Chat"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatAction(RootObject):
    __tdlib_type__ = "ChatAction"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatActionBar(RootObject):
    __tdlib_type__ = "ChatActionBar"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatAdministrator(RootObject):
    __tdlib_type__ = "ChatAdministrator"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatAdministrators(RootObject):
    __tdlib_type__ = "ChatAdministrators"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatEvent(RootObject):
    __tdlib_type__ = "ChatEvent"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatEventAction(RootObject):
    __tdlib_type__ = "ChatEventAction"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatEventLogFilters(RootObject):
    __tdlib_type__ = "ChatEventLogFilters"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatEvents(RootObject):
    __tdlib_type__ = "ChatEvents"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatInviteLink(RootObject):
    __tdlib_type__ = "ChatInviteLink"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatInviteLinkInfo(RootObject):
    __tdlib_type__ = "ChatInviteLinkInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatList(RootObject):
    __tdlib_type__ = "ChatList"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatLocation(RootObject):
    __tdlib_type__ = "ChatLocation"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatMember(RootObject):
    __tdlib_type__ = "ChatMember"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatMemberStatus(RootObject):
    __tdlib_type__ = "ChatMemberStatus"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatMembers(RootObject):
    __tdlib_type__ = "ChatMembers"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatMembersFilter(RootObject):
    __tdlib_type__ = "ChatMembersFilter"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatNearby(RootObject):
    __tdlib_type__ = "ChatNearby"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatNotificationSettings(RootObject):
    __tdlib_type__ = "ChatNotificationSettings"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatPermissions(RootObject):
    __tdlib_type__ = "ChatPermissions"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatPhoto(RootObject):
    __tdlib_type__ = "ChatPhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatReportReason(RootObject):
    __tdlib_type__ = "ChatReportReason"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatType(RootObject):
    __tdlib_type__ = "ChatType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Chats(RootObject):
    __tdlib_type__ = "Chats"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ChatsNearby(RootObject):
    __tdlib_type__ = "ChatsNearby"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class CheckChatUsernameResult(RootObject):
    __tdlib_type__ = "CheckChatUsernameResult"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ConnectedWebsite(RootObject):
    __tdlib_type__ = "ConnectedWebsite"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ConnectedWebsites(RootObject):
    __tdlib_type__ = "ConnectedWebsites"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ConnectionState(RootObject):
    __tdlib_type__ = "ConnectionState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Contact(RootObject):
    __tdlib_type__ = "Contact"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Count(RootObject):
    __tdlib_type__ = "Count"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class CustomRequestResult(RootObject):
    __tdlib_type__ = "CustomRequestResult"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class DatabaseStatistics(RootObject):
    __tdlib_type__ = "DatabaseStatistics"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Date(RootObject):
    __tdlib_type__ = "Date"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class DatedFile(RootObject):
    __tdlib_type__ = "DatedFile"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class DeepLinkInfo(RootObject):
    __tdlib_type__ = "DeepLinkInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class DeviceToken(RootObject):
    __tdlib_type__ = "DeviceToken"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Document(RootObject):
    __tdlib_type__ = "Document"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class DraftMessage(RootObject):
    __tdlib_type__ = "DraftMessage"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class EmailAddressAuthenticationCodeInfo(RootObject):
    __tdlib_type__ = "EmailAddressAuthenticationCodeInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Emojis(RootObject):
    __tdlib_type__ = "Emojis"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class EncryptedCredentials(RootObject):
    __tdlib_type__ = "EncryptedCredentials"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class EncryptedPassportElement(RootObject):
    __tdlib_type__ = "EncryptedPassportElement"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Error(RootObject):
    __tdlib_type__ = "Error"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class File(RootObject):
    __tdlib_type__ = "File"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class FilePart(RootObject):
    __tdlib_type__ = "FilePart"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class FileType(RootObject):
    __tdlib_type__ = "FileType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class FormattedText(RootObject):
    __tdlib_type__ = "FormattedText"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class FoundMessages(RootObject):
    __tdlib_type__ = "FoundMessages"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Game(RootObject):
    __tdlib_type__ = "Game"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class GameHighScore(RootObject):
    __tdlib_type__ = "GameHighScore"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class GameHighScores(RootObject):
    __tdlib_type__ = "GameHighScores"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Hashtags(RootObject):
    __tdlib_type__ = "Hashtags"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class HttpUrl(RootObject):
    __tdlib_type__ = "HttpUrl"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class IdentityDocument(RootObject):
    __tdlib_type__ = "IdentityDocument"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ImportedContacts(RootObject):
    __tdlib_type__ = "ImportedContacts"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InlineKeyboardButton(RootObject):
    __tdlib_type__ = "InlineKeyboardButton"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InlineKeyboardButtonType(RootObject):
    __tdlib_type__ = "InlineKeyboardButtonType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InlineQueryResult(RootObject):
    __tdlib_type__ = "InlineQueryResult"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InlineQueryResults(RootObject):
    __tdlib_type__ = "InlineQueryResults"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InputBackground(RootObject):
    __tdlib_type__ = "InputBackground"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InputCredentials(RootObject):
    __tdlib_type__ = "InputCredentials"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InputFile(RootObject):
    __tdlib_type__ = "InputFile"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InputIdentityDocument(RootObject):
    __tdlib_type__ = "InputIdentityDocument"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InputInlineQueryResult(RootObject):
    __tdlib_type__ = "InputInlineQueryResult"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InputMessageContent(RootObject):
    __tdlib_type__ = "InputMessageContent"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InputPassportElement(RootObject):
    __tdlib_type__ = "InputPassportElement"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InputPassportElementError(RootObject):
    __tdlib_type__ = "InputPassportElementError"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InputPassportElementErrorSource(RootObject):
    __tdlib_type__ = "InputPassportElementErrorSource"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InputPersonalDocument(RootObject):
    __tdlib_type__ = "InputPersonalDocument"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InputSticker(RootObject):
    __tdlib_type__ = "InputSticker"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InputThumbnail(RootObject):
    __tdlib_type__ = "InputThumbnail"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Invoice(RootObject):
    __tdlib_type__ = "Invoice"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class JsonObjectMember(RootObject):
    __tdlib_type__ = "JsonObjectMember"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class JsonValue(RootObject):
    __tdlib_type__ = "JsonValue"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class KeyboardButton(RootObject):
    __tdlib_type__ = "KeyboardButton"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class KeyboardButtonType(RootObject):
    __tdlib_type__ = "KeyboardButtonType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class LabeledPricePart(RootObject):
    __tdlib_type__ = "LabeledPricePart"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class LanguagePackInfo(RootObject):
    __tdlib_type__ = "LanguagePackInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class LanguagePackString(RootObject):
    __tdlib_type__ = "LanguagePackString"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class LanguagePackStringValue(RootObject):
    __tdlib_type__ = "LanguagePackStringValue"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class LanguagePackStrings(RootObject):
    __tdlib_type__ = "LanguagePackStrings"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class LocalFile(RootObject):
    __tdlib_type__ = "LocalFile"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class LocalizationTargetInfo(RootObject):
    __tdlib_type__ = "LocalizationTargetInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Location(RootObject):
    __tdlib_type__ = "Location"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class LogStream(RootObject):
    __tdlib_type__ = "LogStream"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class LogTags(RootObject):
    __tdlib_type__ = "LogTags"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class LogVerbosityLevel(RootObject):
    __tdlib_type__ = "LogVerbosityLevel"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class LoginUrlInfo(RootObject):
    __tdlib_type__ = "LoginUrlInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class MaskPoint(RootObject):
    __tdlib_type__ = "MaskPoint"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class MaskPosition(RootObject):
    __tdlib_type__ = "MaskPosition"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Message(RootObject):
    __tdlib_type__ = "Message"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class MessageContent(RootObject):
    __tdlib_type__ = "MessageContent"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class MessageForwardInfo(RootObject):
    __tdlib_type__ = "MessageForwardInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class MessageForwardOrigin(RootObject):
    __tdlib_type__ = "MessageForwardOrigin"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class MessageLinkInfo(RootObject):
    __tdlib_type__ = "MessageLinkInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class MessageSchedulingState(RootObject):
    __tdlib_type__ = "MessageSchedulingState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class MessageSendingState(RootObject):
    __tdlib_type__ = "MessageSendingState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Messages(RootObject):
    __tdlib_type__ = "Messages"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Minithumbnail(RootObject):
    __tdlib_type__ = "Minithumbnail"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class NetworkStatistics(RootObject):
    __tdlib_type__ = "NetworkStatistics"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class NetworkStatisticsEntry(RootObject):
    __tdlib_type__ = "NetworkStatisticsEntry"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class NetworkType(RootObject):
    __tdlib_type__ = "NetworkType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Notification(RootObject):
    __tdlib_type__ = "Notification"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class NotificationGroup(RootObject):
    __tdlib_type__ = "NotificationGroup"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class NotificationGroupType(RootObject):
    __tdlib_type__ = "NotificationGroupType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class NotificationSettingsScope(RootObject):
    __tdlib_type__ = "NotificationSettingsScope"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class NotificationType(RootObject):
    __tdlib_type__ = "NotificationType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Ok(RootObject):
    __tdlib_type__ = "Ok"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class OptionValue(RootObject):
    __tdlib_type__ = "OptionValue"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class OrderInfo(RootObject):
    __tdlib_type__ = "OrderInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PageBlock(RootObject):
    __tdlib_type__ = "PageBlock"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PageBlockCaption(RootObject):
    __tdlib_type__ = "PageBlockCaption"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PageBlockHorizontalAlignment(RootObject):
    __tdlib_type__ = "PageBlockHorizontalAlignment"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PageBlockListItem(RootObject):
    __tdlib_type__ = "PageBlockListItem"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PageBlockRelatedArticle(RootObject):
    __tdlib_type__ = "PageBlockRelatedArticle"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PageBlockTableCell(RootObject):
    __tdlib_type__ = "PageBlockTableCell"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PageBlockVerticalAlignment(RootObject):
    __tdlib_type__ = "PageBlockVerticalAlignment"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PassportAuthorizationForm(RootObject):
    __tdlib_type__ = "PassportAuthorizationForm"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PassportElement(RootObject):
    __tdlib_type__ = "PassportElement"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PassportElementError(RootObject):
    __tdlib_type__ = "PassportElementError"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PassportElementErrorSource(RootObject):
    __tdlib_type__ = "PassportElementErrorSource"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PassportElementType(RootObject):
    __tdlib_type__ = "PassportElementType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PassportElements(RootObject):
    __tdlib_type__ = "PassportElements"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PassportElementsWithErrors(RootObject):
    __tdlib_type__ = "PassportElementsWithErrors"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PassportRequiredElement(RootObject):
    __tdlib_type__ = "PassportRequiredElement"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PassportSuitableElement(RootObject):
    __tdlib_type__ = "PassportSuitableElement"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PasswordState(RootObject):
    __tdlib_type__ = "PasswordState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PaymentForm(RootObject):
    __tdlib_type__ = "PaymentForm"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PaymentReceipt(RootObject):
    __tdlib_type__ = "PaymentReceipt"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PaymentResult(RootObject):
    __tdlib_type__ = "PaymentResult"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PaymentsProviderStripe(RootObject):
    __tdlib_type__ = "PaymentsProviderStripe"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PersonalDetails(RootObject):
    __tdlib_type__ = "PersonalDetails"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PersonalDocument(RootObject):
    __tdlib_type__ = "PersonalDocument"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PhoneNumberAuthenticationSettings(RootObject):
    __tdlib_type__ = "PhoneNumberAuthenticationSettings"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Photo(RootObject):
    __tdlib_type__ = "Photo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PhotoSize(RootObject):
    __tdlib_type__ = "PhotoSize"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Poll(RootObject):
    __tdlib_type__ = "Poll"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PollOption(RootObject):
    __tdlib_type__ = "PollOption"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ProfilePhoto(RootObject):
    __tdlib_type__ = "ProfilePhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Proxies(RootObject):
    __tdlib_type__ = "Proxies"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Proxy(RootObject):
    __tdlib_type__ = "Proxy"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ProxyType(RootObject):
    __tdlib_type__ = "ProxyType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PublicChatType(RootObject):
    __tdlib_type__ = "PublicChatType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PublicMessageLink(RootObject):
    __tdlib_type__ = "PublicMessageLink"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PushMessageContent(RootObject):
    __tdlib_type__ = "PushMessageContent"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PushReceiverId(RootObject):
    __tdlib_type__ = "PushReceiverId"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class RecoveryEmailAddress(RootObject):
    __tdlib_type__ = "RecoveryEmailAddress"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class RemoteFile(RootObject):
    __tdlib_type__ = "RemoteFile"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ReplyMarkup(RootObject):
    __tdlib_type__ = "ReplyMarkup"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class RichText(RootObject):
    __tdlib_type__ = "RichText"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class SavedCredentials(RootObject):
    __tdlib_type__ = "SavedCredentials"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ScopeNotificationSettings(RootObject):
    __tdlib_type__ = "ScopeNotificationSettings"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class SearchMessagesFilter(RootObject):
    __tdlib_type__ = "SearchMessagesFilter"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Seconds(RootObject):
    __tdlib_type__ = "Seconds"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class SecretChat(RootObject):
    __tdlib_type__ = "SecretChat"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class SecretChatState(RootObject):
    __tdlib_type__ = "SecretChatState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class SendMessageOptions(RootObject):
    __tdlib_type__ = "SendMessageOptions"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Session(RootObject):
    __tdlib_type__ = "Session"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Sessions(RootObject):
    __tdlib_type__ = "Sessions"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ShippingOption(RootObject):
    __tdlib_type__ = "ShippingOption"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Sticker(RootObject):
    __tdlib_type__ = "Sticker"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class StickerSet(RootObject):
    __tdlib_type__ = "StickerSet"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class StickerSetInfo(RootObject):
    __tdlib_type__ = "StickerSetInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class StickerSets(RootObject):
    __tdlib_type__ = "StickerSets"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Stickers(RootObject):
    __tdlib_type__ = "Stickers"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class StorageStatistics(RootObject):
    __tdlib_type__ = "StorageStatistics"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class StorageStatisticsByChat(RootObject):
    __tdlib_type__ = "StorageStatisticsByChat"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class StorageStatisticsByFileType(RootObject):
    __tdlib_type__ = "StorageStatisticsByFileType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class StorageStatisticsFast(RootObject):
    __tdlib_type__ = "StorageStatisticsFast"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Supergroup(RootObject):
    __tdlib_type__ = "Supergroup"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class SupergroupFullInfo(RootObject):
    __tdlib_type__ = "SupergroupFullInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class SupergroupMembersFilter(RootObject):
    __tdlib_type__ = "SupergroupMembersFilter"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TMeUrl(RootObject):
    __tdlib_type__ = "TMeUrl"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TMeUrlType(RootObject):
    __tdlib_type__ = "TMeUrlType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TMeUrls(RootObject):
    __tdlib_type__ = "TMeUrls"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TdlibParameters(RootObject):
    __tdlib_type__ = "TdlibParameters"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TemporaryPasswordState(RootObject):
    __tdlib_type__ = "TemporaryPasswordState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TermsOfService(RootObject):
    __tdlib_type__ = "TermsOfService"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TestBytes(RootObject):
    __tdlib_type__ = "TestBytes"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TestInt(RootObject):
    __tdlib_type__ = "TestInt"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TestString(RootObject):
    __tdlib_type__ = "TestString"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TestVectorInt(RootObject):
    __tdlib_type__ = "TestVectorInt"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TestVectorIntObject(RootObject):
    __tdlib_type__ = "TestVectorIntObject"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TestVectorString(RootObject):
    __tdlib_type__ = "TestVectorString"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TestVectorStringObject(RootObject):
    __tdlib_type__ = "TestVectorStringObject"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Text(RootObject):
    __tdlib_type__ = "Text"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TextEntities(RootObject):
    __tdlib_type__ = "TextEntities"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TextEntity(RootObject):
    __tdlib_type__ = "TextEntity"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TextEntityType(RootObject):
    __tdlib_type__ = "TextEntityType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TextParseMode(RootObject):
    __tdlib_type__ = "TextParseMode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TonLiteServerResponse(RootObject):
    __tdlib_type__ = "TonLiteServerResponse"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TonWalletPasswordSalt(RootObject):
    __tdlib_type__ = "TonWalletPasswordSalt"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TopChatCategory(RootObject):
    __tdlib_type__ = "TopChatCategory"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Update(RootObject):
    __tdlib_type__ = "Update"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Updates(RootObject):
    __tdlib_type__ = "Updates"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class User(RootObject):
    __tdlib_type__ = "User"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class UserFullInfo(RootObject):
    __tdlib_type__ = "UserFullInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class UserPrivacySetting(RootObject):
    __tdlib_type__ = "UserPrivacySetting"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class UserPrivacySettingRule(RootObject):
    __tdlib_type__ = "UserPrivacySettingRule"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class UserPrivacySettingRules(RootObject):
    __tdlib_type__ = "UserPrivacySettingRules"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class UserProfilePhoto(RootObject):
    __tdlib_type__ = "UserProfilePhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class UserProfilePhotos(RootObject):
    __tdlib_type__ = "UserProfilePhotos"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class UserStatus(RootObject):
    __tdlib_type__ = "UserStatus"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class UserType(RootObject):
    __tdlib_type__ = "UserType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Users(RootObject):
    __tdlib_type__ = "Users"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ValidatedOrderInfo(RootObject):
    __tdlib_type__ = "ValidatedOrderInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Venue(RootObject):
    __tdlib_type__ = "Venue"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class Video(RootObject):
    __tdlib_type__ = "Video"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class VideoNote(RootObject):
    __tdlib_type__ = "VideoNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class VoiceNote(RootObject):
    __tdlib_type__ = "VoiceNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class WebPage(RootObject):
    __tdlib_type__ = "WebPage"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class WebPageInstantView(RootObject):
    __tdlib_type__ = "WebPageInstantView"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class accountTtl(AccountTtl):
    __tdlib_type__ = "accountTtl"
    days: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class address(Address):
    __tdlib_type__ = "address"
    country_code: str = attr.ib()
    state: str = attr.ib()
    city: str = attr.ib()
    street_line1: str = attr.ib()
    street_line2: str = attr.ib()
    postal_code: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class animation(Animation):
    __tdlib_type__ = "animation"
    duration: int = attr.ib()
    width: int = attr.ib()
    height: int = attr.ib()
    file_name: str = attr.ib()
    mime_type: str = attr.ib()
    minithumbnail: minithumbnail = attr.ib()
    thumbnail: photoSize = attr.ib()
    animation: file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class animations(Animations):
    __tdlib_type__ = "animations"
    animations: typing.Sequence[animation] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class audio(Audio):
    __tdlib_type__ = "audio"
    duration: int = attr.ib()
    title: str = attr.ib()
    performer: str = attr.ib()
    file_name: str = attr.ib()
    mime_type: str = attr.ib()
    album_cover_minithumbnail: minithumbnail = attr.ib()
    album_cover_thumbnail: photoSize = attr.ib()
    audio: file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authenticationCodeInfo(AuthenticationCodeInfo):
    __tdlib_type__ = "authenticationCodeInfo"
    phone_number: str = attr.ib()
    type: AuthenticationCodeType = attr.ib()
    next_type: AuthenticationCodeType = attr.ib()
    timeout: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authenticationCodeTypeCall(AuthenticationCodeType):
    __tdlib_type__ = "authenticationCodeTypeCall"
    length: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authenticationCodeTypeFlashCall(AuthenticationCodeType):
    __tdlib_type__ = "authenticationCodeTypeFlashCall"
    pattern: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authenticationCodeTypeSms(AuthenticationCodeType):
    __tdlib_type__ = "authenticationCodeTypeSms"
    length: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authenticationCodeTypeTelegramMessage(AuthenticationCodeType):
    __tdlib_type__ = "authenticationCodeTypeTelegramMessage"
    length: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authorizationStateClosed(AuthorizationState):
    __tdlib_type__ = "authorizationStateClosed"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authorizationStateClosing(AuthorizationState):
    __tdlib_type__ = "authorizationStateClosing"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authorizationStateLoggingOut(AuthorizationState):
    __tdlib_type__ = "authorizationStateLoggingOut"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authorizationStateReady(AuthorizationState):
    __tdlib_type__ = "authorizationStateReady"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authorizationStateWaitCode(AuthorizationState):
    __tdlib_type__ = "authorizationStateWaitCode"
    code_info: authenticationCodeInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authorizationStateWaitEncryptionKey(AuthorizationState):
    __tdlib_type__ = "authorizationStateWaitEncryptionKey"
    is_encrypted: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authorizationStateWaitOtherDeviceConfirmation(AuthorizationState):
    __tdlib_type__ = "authorizationStateWaitOtherDeviceConfirmation"
    link: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authorizationStateWaitPassword(AuthorizationState):
    __tdlib_type__ = "authorizationStateWaitPassword"
    password_hint: str = attr.ib()
    has_recovery_email_address: bool = attr.ib()
    recovery_email_address_pattern: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authorizationStateWaitPhoneNumber(AuthorizationState):
    __tdlib_type__ = "authorizationStateWaitPhoneNumber"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authorizationStateWaitRegistration(AuthorizationState):
    __tdlib_type__ = "authorizationStateWaitRegistration"
    terms_of_service: termsOfService = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class authorizationStateWaitTdlibParameters(AuthorizationState):
    __tdlib_type__ = "authorizationStateWaitTdlibParameters"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class autoDownloadSettings(AutoDownloadSettings):
    __tdlib_type__ = "autoDownloadSettings"
    is_auto_download_enabled: bool = attr.ib()
    max_photo_file_size: int = attr.ib()
    max_video_file_size: int = attr.ib()
    max_other_file_size: int = attr.ib()
    video_upload_bitrate: int = attr.ib()
    preload_large_videos: bool = attr.ib()
    preload_next_audio: bool = attr.ib()
    use_less_data_for_calls: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class autoDownloadSettingsPresets(AutoDownloadSettingsPresets):
    __tdlib_type__ = "autoDownloadSettingsPresets"
    low: autoDownloadSettings = attr.ib()
    medium: autoDownloadSettings = attr.ib()
    high: autoDownloadSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class background(Background):
    __tdlib_type__ = "background"
    id: int = attr.ib()
    is_default: bool = attr.ib()
    is_dark: bool = attr.ib()
    name: str = attr.ib()
    document: document = attr.ib()
    type: BackgroundType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class backgroundFillGradient(BackgroundFill):
    __tdlib_type__ = "backgroundFillGradient"
    top_color: int = attr.ib()
    bottom_color: int = attr.ib()
    rotation_angle: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class backgroundFillSolid(BackgroundFill):
    __tdlib_type__ = "backgroundFillSolid"
    color: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class backgroundTypeFill(BackgroundType):
    __tdlib_type__ = "backgroundTypeFill"
    fill: BackgroundFill = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class backgroundTypePattern(BackgroundType):
    __tdlib_type__ = "backgroundTypePattern"
    fill: BackgroundFill = attr.ib()
    intensity: int = attr.ib()
    is_moving: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class backgroundTypeWallpaper(BackgroundType):
    __tdlib_type__ = "backgroundTypeWallpaper"
    is_blurred: bool = attr.ib()
    is_moving: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class backgrounds(Backgrounds):
    __tdlib_type__ = "backgrounds"
    backgrounds: typing.Sequence[background] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class basicGroup(BasicGroup):
    __tdlib_type__ = "basicGroup"
    id: int = attr.ib()
    member_count: int = attr.ib()
    status: ChatMemberStatus = attr.ib()
    is_active: bool = attr.ib()
    upgraded_to_supergroup_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class basicGroupFullInfo(BasicGroupFullInfo):
    __tdlib_type__ = "basicGroupFullInfo"
    description: str = attr.ib()
    creator_user_id: int = attr.ib()
    members: typing.Sequence[chatMember] = attr.ib()
    invite_link: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class botCommand(BotCommand):
    __tdlib_type__ = "botCommand"
    command: str = attr.ib()
    description: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class botInfo(BotInfo):
    __tdlib_type__ = "botInfo"
    description: str = attr.ib()
    commands: typing.Sequence[botCommand] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class call(Call):
    __tdlib_type__ = "call"
    id: int = attr.ib()
    user_id: int = attr.ib()
    is_outgoing: bool = attr.ib()
    state: CallState = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callConnection(CallConnection):
    __tdlib_type__ = "callConnection"
    id: int = attr.ib()
    ip: str = attr.ib()
    ipv6: str = attr.ib()
    port: int = attr.ib()
    peer_tag: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callDiscardReasonDeclined(CallDiscardReason):
    __tdlib_type__ = "callDiscardReasonDeclined"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callDiscardReasonDisconnected(CallDiscardReason):
    __tdlib_type__ = "callDiscardReasonDisconnected"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callDiscardReasonEmpty(CallDiscardReason):
    __tdlib_type__ = "callDiscardReasonEmpty"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callDiscardReasonHungUp(CallDiscardReason):
    __tdlib_type__ = "callDiscardReasonHungUp"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callDiscardReasonMissed(CallDiscardReason):
    __tdlib_type__ = "callDiscardReasonMissed"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callId(CallId):
    __tdlib_type__ = "callId"
    id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callProblemDistortedSpeech(CallProblem):
    __tdlib_type__ = "callProblemDistortedSpeech"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callProblemDropped(CallProblem):
    __tdlib_type__ = "callProblemDropped"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callProblemEcho(CallProblem):
    __tdlib_type__ = "callProblemEcho"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callProblemInterruptions(CallProblem):
    __tdlib_type__ = "callProblemInterruptions"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callProblemNoise(CallProblem):
    __tdlib_type__ = "callProblemNoise"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callProblemSilentLocal(CallProblem):
    __tdlib_type__ = "callProblemSilentLocal"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callProblemSilentRemote(CallProblem):
    __tdlib_type__ = "callProblemSilentRemote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callProtocol(CallProtocol):
    __tdlib_type__ = "callProtocol"
    udp_p2p: bool = attr.ib()
    udp_reflector: bool = attr.ib()
    min_layer: int = attr.ib()
    max_layer: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callStateDiscarded(CallState):
    __tdlib_type__ = "callStateDiscarded"
    reason: CallDiscardReason = attr.ib()
    need_rating: bool = attr.ib()
    need_debug_information: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callStateError(CallState):
    __tdlib_type__ = "callStateError"
    error: error = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callStateExchangingKeys(CallState):
    __tdlib_type__ = "callStateExchangingKeys"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callStateHangingUp(CallState):
    __tdlib_type__ = "callStateHangingUp"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callStatePending(CallState):
    __tdlib_type__ = "callStatePending"
    is_created: bool = attr.ib()
    is_received: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callStateReady(CallState):
    __tdlib_type__ = "callStateReady"
    protocol: callProtocol = attr.ib()
    connections: typing.Sequence[callConnection] = attr.ib()
    config: str = attr.ib()
    encryption_key: bytes = attr.ib()
    emojis: typing.Sequence[str] = attr.ib()
    allow_p2p: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callbackQueryAnswer(CallbackQueryAnswer):
    __tdlib_type__ = "callbackQueryAnswer"
    text: str = attr.ib()
    show_alert: bool = attr.ib()
    url: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callbackQueryPayloadData(CallbackQueryPayload):
    __tdlib_type__ = "callbackQueryPayloadData"
    data: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class callbackQueryPayloadGame(CallbackQueryPayload):
    __tdlib_type__ = "callbackQueryPayloadGame"
    game_short_name: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class canTransferOwnershipResultOk(CanTransferOwnershipResult):
    __tdlib_type__ = "canTransferOwnershipResultOk"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class canTransferOwnershipResultPasswordNeeded(CanTransferOwnershipResult):
    __tdlib_type__ = "canTransferOwnershipResultPasswordNeeded"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class canTransferOwnershipResultPasswordTooFresh(CanTransferOwnershipResult):
    __tdlib_type__ = "canTransferOwnershipResultPasswordTooFresh"
    retry_after: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class canTransferOwnershipResultSessionTooFresh(CanTransferOwnershipResult):
    __tdlib_type__ = "canTransferOwnershipResultSessionTooFresh"
    retry_after: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chat(Chat):
    __tdlib_type__ = "chat"
    id: int = attr.ib()
    type: ChatType = attr.ib()
    chat_list: ChatList = attr.ib()
    title: str = attr.ib()
    photo: chatPhoto = attr.ib()
    permissions: chatPermissions = attr.ib()
    last_message: message = attr.ib()
    order: int = attr.ib()
    is_pinned: bool = attr.ib()
    is_marked_as_unread: bool = attr.ib()
    is_sponsored: bool = attr.ib()
    has_scheduled_messages: bool = attr.ib()
    can_be_deleted_only_for_self: bool = attr.ib()
    can_be_deleted_for_all_users: bool = attr.ib()
    can_be_reported: bool = attr.ib()
    default_disable_notification: bool = attr.ib()
    unread_count: int = attr.ib()
    last_read_inbox_message_id: int = attr.ib()
    last_read_outbox_message_id: int = attr.ib()
    unread_mention_count: int = attr.ib()
    notification_settings: chatNotificationSettings = attr.ib()
    action_bar: ChatActionBar = attr.ib()
    pinned_message_id: int = attr.ib()
    reply_markup_message_id: int = attr.ib()
    draft_message: draftMessage = attr.ib()
    client_data: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionBarAddContact(ChatActionBar):
    __tdlib_type__ = "chatActionBarAddContact"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionBarReportAddBlock(ChatActionBar):
    __tdlib_type__ = "chatActionBarReportAddBlock"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionBarReportSpam(ChatActionBar):
    __tdlib_type__ = "chatActionBarReportSpam"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionBarReportUnrelatedLocation(ChatActionBar):
    __tdlib_type__ = "chatActionBarReportUnrelatedLocation"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionBarSharePhoneNumber(ChatActionBar):
    __tdlib_type__ = "chatActionBarSharePhoneNumber"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionCancel(ChatAction):
    __tdlib_type__ = "chatActionCancel"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionChoosingContact(ChatAction):
    __tdlib_type__ = "chatActionChoosingContact"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionChoosingLocation(ChatAction):
    __tdlib_type__ = "chatActionChoosingLocation"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionRecordingVideo(ChatAction):
    __tdlib_type__ = "chatActionRecordingVideo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionRecordingVideoNote(ChatAction):
    __tdlib_type__ = "chatActionRecordingVideoNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionRecordingVoiceNote(ChatAction):
    __tdlib_type__ = "chatActionRecordingVoiceNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionStartPlayingGame(ChatAction):
    __tdlib_type__ = "chatActionStartPlayingGame"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionTyping(ChatAction):
    __tdlib_type__ = "chatActionTyping"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionUploadingDocument(ChatAction):
    __tdlib_type__ = "chatActionUploadingDocument"
    progress: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionUploadingPhoto(ChatAction):
    __tdlib_type__ = "chatActionUploadingPhoto"
    progress: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionUploadingVideo(ChatAction):
    __tdlib_type__ = "chatActionUploadingVideo"
    progress: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionUploadingVideoNote(ChatAction):
    __tdlib_type__ = "chatActionUploadingVideoNote"
    progress: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatActionUploadingVoiceNote(ChatAction):
    __tdlib_type__ = "chatActionUploadingVoiceNote"
    progress: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatAdministrator(ChatAdministrator):
    __tdlib_type__ = "chatAdministrator"
    user_id: int = attr.ib()
    custom_title: str = attr.ib()
    is_owner: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatAdministrators(ChatAdministrators):
    __tdlib_type__ = "chatAdministrators"
    administrators: typing.Sequence[chatAdministrator] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEvent(ChatEvent):
    __tdlib_type__ = "chatEvent"
    id: int = attr.ib()
    date: int = attr.ib()
    user_id: int = attr.ib()
    action: ChatEventAction = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventDescriptionChanged(ChatEventAction):
    __tdlib_type__ = "chatEventDescriptionChanged"
    old_description: str = attr.ib()
    new_description: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventInvitesToggled(ChatEventAction):
    __tdlib_type__ = "chatEventInvitesToggled"
    can_invite_users: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventIsAllHistoryAvailableToggled(ChatEventAction):
    __tdlib_type__ = "chatEventIsAllHistoryAvailableToggled"
    is_all_history_available: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventLinkedChatChanged(ChatEventAction):
    __tdlib_type__ = "chatEventLinkedChatChanged"
    old_linked_chat_id: int = attr.ib()
    new_linked_chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventLocationChanged(ChatEventAction):
    __tdlib_type__ = "chatEventLocationChanged"
    old_location: chatLocation = attr.ib()
    new_location: chatLocation = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventLogFilters(ChatEventLogFilters):
    __tdlib_type__ = "chatEventLogFilters"
    message_edits: bool = attr.ib()
    message_deletions: bool = attr.ib()
    message_pins: bool = attr.ib()
    member_joins: bool = attr.ib()
    member_leaves: bool = attr.ib()
    member_invites: bool = attr.ib()
    member_promotions: bool = attr.ib()
    member_restrictions: bool = attr.ib()
    info_changes: bool = attr.ib()
    setting_changes: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventMemberInvited(ChatEventAction):
    __tdlib_type__ = "chatEventMemberInvited"
    user_id: int = attr.ib()
    status: ChatMemberStatus = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventMemberJoined(ChatEventAction):
    __tdlib_type__ = "chatEventMemberJoined"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventMemberLeft(ChatEventAction):
    __tdlib_type__ = "chatEventMemberLeft"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventMemberPromoted(ChatEventAction):
    __tdlib_type__ = "chatEventMemberPromoted"
    user_id: int = attr.ib()
    old_status: ChatMemberStatus = attr.ib()
    new_status: ChatMemberStatus = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventMemberRestricted(ChatEventAction):
    __tdlib_type__ = "chatEventMemberRestricted"
    user_id: int = attr.ib()
    old_status: ChatMemberStatus = attr.ib()
    new_status: ChatMemberStatus = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventMessageDeleted(ChatEventAction):
    __tdlib_type__ = "chatEventMessageDeleted"
    message: message = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventMessageEdited(ChatEventAction):
    __tdlib_type__ = "chatEventMessageEdited"
    old_message: message = attr.ib()
    new_message: message = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventMessagePinned(ChatEventAction):
    __tdlib_type__ = "chatEventMessagePinned"
    message: message = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventMessageUnpinned(ChatEventAction):
    __tdlib_type__ = "chatEventMessageUnpinned"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventPermissionsChanged(ChatEventAction):
    __tdlib_type__ = "chatEventPermissionsChanged"
    old_permissions: chatPermissions = attr.ib()
    new_permissions: chatPermissions = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventPhotoChanged(ChatEventAction):
    __tdlib_type__ = "chatEventPhotoChanged"
    old_photo: photo = attr.ib()
    new_photo: photo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventPollStopped(ChatEventAction):
    __tdlib_type__ = "chatEventPollStopped"
    message: message = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventSignMessagesToggled(ChatEventAction):
    __tdlib_type__ = "chatEventSignMessagesToggled"
    sign_messages: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventSlowModeDelayChanged(ChatEventAction):
    __tdlib_type__ = "chatEventSlowModeDelayChanged"
    old_slow_mode_delay: int = attr.ib()
    new_slow_mode_delay: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventStickerSetChanged(ChatEventAction):
    __tdlib_type__ = "chatEventStickerSetChanged"
    old_sticker_set_id: int = attr.ib()
    new_sticker_set_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventTitleChanged(ChatEventAction):
    __tdlib_type__ = "chatEventTitleChanged"
    old_title: str = attr.ib()
    new_title: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEventUsernameChanged(ChatEventAction):
    __tdlib_type__ = "chatEventUsernameChanged"
    old_username: str = attr.ib()
    new_username: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatEvents(ChatEvents):
    __tdlib_type__ = "chatEvents"
    events: typing.Sequence[chatEvent] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatInviteLink(ChatInviteLink):
    __tdlib_type__ = "chatInviteLink"
    invite_link: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatInviteLinkInfo(ChatInviteLinkInfo):
    __tdlib_type__ = "chatInviteLinkInfo"
    chat_id: int = attr.ib()
    type: ChatType = attr.ib()
    title: str = attr.ib()
    photo: chatPhoto = attr.ib()
    member_count: int = attr.ib()
    member_user_ids: typing.Sequence[int] = attr.ib()
    is_public: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatListArchive(ChatList):
    __tdlib_type__ = "chatListArchive"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatListMain(ChatList):
    __tdlib_type__ = "chatListMain"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatLocation(ChatLocation):
    __tdlib_type__ = "chatLocation"
    location: location = attr.ib()
    address: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatMember(ChatMember):
    __tdlib_type__ = "chatMember"
    user_id: int = attr.ib()
    inviter_user_id: int = attr.ib()
    joined_chat_date: int = attr.ib()
    status: ChatMemberStatus = attr.ib()
    bot_info: botInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatMemberStatusAdministrator(ChatMemberStatus):
    __tdlib_type__ = "chatMemberStatusAdministrator"
    custom_title: str = attr.ib()
    can_be_edited: bool = attr.ib()
    can_change_info: bool = attr.ib()
    can_post_messages: bool = attr.ib()
    can_edit_messages: bool = attr.ib()
    can_delete_messages: bool = attr.ib()
    can_invite_users: bool = attr.ib()
    can_restrict_members: bool = attr.ib()
    can_pin_messages: bool = attr.ib()
    can_promote_members: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatMemberStatusBanned(ChatMemberStatus):
    __tdlib_type__ = "chatMemberStatusBanned"
    banned_until_date: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatMemberStatusCreator(ChatMemberStatus):
    __tdlib_type__ = "chatMemberStatusCreator"
    custom_title: str = attr.ib()
    is_member: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatMemberStatusLeft(ChatMemberStatus):
    __tdlib_type__ = "chatMemberStatusLeft"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatMemberStatusMember(ChatMemberStatus):
    __tdlib_type__ = "chatMemberStatusMember"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatMemberStatusRestricted(ChatMemberStatus):
    __tdlib_type__ = "chatMemberStatusRestricted"
    is_member: bool = attr.ib()
    restricted_until_date: int = attr.ib()
    permissions: chatPermissions = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatMembers(ChatMembers):
    __tdlib_type__ = "chatMembers"
    total_count: int = attr.ib()
    members: typing.Sequence[chatMember] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatMembersFilterAdministrators(ChatMembersFilter):
    __tdlib_type__ = "chatMembersFilterAdministrators"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatMembersFilterBanned(ChatMembersFilter):
    __tdlib_type__ = "chatMembersFilterBanned"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatMembersFilterBots(ChatMembersFilter):
    __tdlib_type__ = "chatMembersFilterBots"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatMembersFilterContacts(ChatMembersFilter):
    __tdlib_type__ = "chatMembersFilterContacts"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatMembersFilterMembers(ChatMembersFilter):
    __tdlib_type__ = "chatMembersFilterMembers"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatMembersFilterRestricted(ChatMembersFilter):
    __tdlib_type__ = "chatMembersFilterRestricted"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatNearby(ChatNearby):
    __tdlib_type__ = "chatNearby"
    chat_id: int = attr.ib()
    distance: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatNotificationSettings(ChatNotificationSettings):
    __tdlib_type__ = "chatNotificationSettings"
    use_default_mute_for: bool = attr.ib()
    mute_for: int = attr.ib()
    use_default_sound: bool = attr.ib()
    sound: str = attr.ib()
    use_default_show_preview: bool = attr.ib()
    show_preview: bool = attr.ib()
    use_default_disable_pinned_message_notifications: bool = attr.ib()
    disable_pinned_message_notifications: bool = attr.ib()
    use_default_disable_mention_notifications: bool = attr.ib()
    disable_mention_notifications: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatPermissions(ChatPermissions):
    __tdlib_type__ = "chatPermissions"
    can_send_messages: bool = attr.ib()
    can_send_media_messages: bool = attr.ib()
    can_send_polls: bool = attr.ib()
    can_send_other_messages: bool = attr.ib()
    can_add_web_page_previews: bool = attr.ib()
    can_change_info: bool = attr.ib()
    can_invite_users: bool = attr.ib()
    can_pin_messages: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatPhoto(ChatPhoto):
    __tdlib_type__ = "chatPhoto"
    small: file = attr.ib()
    big: file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatReportReasonChildAbuse(ChatReportReason):
    __tdlib_type__ = "chatReportReasonChildAbuse"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatReportReasonCopyright(ChatReportReason):
    __tdlib_type__ = "chatReportReasonCopyright"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatReportReasonCustom(ChatReportReason):
    __tdlib_type__ = "chatReportReasonCustom"
    text: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatReportReasonPornography(ChatReportReason):
    __tdlib_type__ = "chatReportReasonPornography"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatReportReasonSpam(ChatReportReason):
    __tdlib_type__ = "chatReportReasonSpam"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatReportReasonUnrelatedLocation(ChatReportReason):
    __tdlib_type__ = "chatReportReasonUnrelatedLocation"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatReportReasonViolence(ChatReportReason):
    __tdlib_type__ = "chatReportReasonViolence"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatTypeBasicGroup(ChatType):
    __tdlib_type__ = "chatTypeBasicGroup"
    basic_group_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatTypePrivate(ChatType):
    __tdlib_type__ = "chatTypePrivate"
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatTypeSecret(ChatType):
    __tdlib_type__ = "chatTypeSecret"
    secret_chat_id: int = attr.ib()
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatTypeSupergroup(ChatType):
    __tdlib_type__ = "chatTypeSupergroup"
    supergroup_id: int = attr.ib()
    is_channel: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chats(Chats):
    __tdlib_type__ = "chats"
    chat_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class chatsNearby(ChatsNearby):
    __tdlib_type__ = "chatsNearby"
    users_nearby: typing.Sequence[chatNearby] = attr.ib()
    supergroups_nearby: typing.Sequence[chatNearby] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkChatUsernameResultOk(CheckChatUsernameResult):
    __tdlib_type__ = "checkChatUsernameResultOk"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkChatUsernameResultPublicChatsTooMuch(CheckChatUsernameResult):
    __tdlib_type__ = "checkChatUsernameResultPublicChatsTooMuch"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkChatUsernameResultPublicGroupsUnavailable(CheckChatUsernameResult):
    __tdlib_type__ = "checkChatUsernameResultPublicGroupsUnavailable"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkChatUsernameResultUsernameInvalid(CheckChatUsernameResult):
    __tdlib_type__ = "checkChatUsernameResultUsernameInvalid"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkChatUsernameResultUsernameOccupied(CheckChatUsernameResult):
    __tdlib_type__ = "checkChatUsernameResultUsernameOccupied"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class connectedWebsite(ConnectedWebsite):
    __tdlib_type__ = "connectedWebsite"
    id: int = attr.ib()
    domain_name: str = attr.ib()
    bot_user_id: int = attr.ib()
    browser: str = attr.ib()
    platform: str = attr.ib()
    log_in_date: int = attr.ib()
    last_active_date: int = attr.ib()
    ip: str = attr.ib()
    location: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class connectedWebsites(ConnectedWebsites):
    __tdlib_type__ = "connectedWebsites"
    websites: typing.Sequence[connectedWebsite] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class connectionStateConnecting(ConnectionState):
    __tdlib_type__ = "connectionStateConnecting"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class connectionStateConnectingToProxy(ConnectionState):
    __tdlib_type__ = "connectionStateConnectingToProxy"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class connectionStateReady(ConnectionState):
    __tdlib_type__ = "connectionStateReady"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class connectionStateUpdating(ConnectionState):
    __tdlib_type__ = "connectionStateUpdating"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class connectionStateWaitingForNetwork(ConnectionState):
    __tdlib_type__ = "connectionStateWaitingForNetwork"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class contact(Contact):
    __tdlib_type__ = "contact"
    phone_number: str = attr.ib()
    first_name: str = attr.ib()
    last_name: str = attr.ib()
    vcard: str = attr.ib()
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class count(Count):
    __tdlib_type__ = "count"
    count: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class customRequestResult(CustomRequestResult):
    __tdlib_type__ = "customRequestResult"
    result: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class databaseStatistics(DatabaseStatistics):
    __tdlib_type__ = "databaseStatistics"
    statistics: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class date(Date):
    __tdlib_type__ = "date"
    day: int = attr.ib()
    month: int = attr.ib()
    year: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class datedFile(DatedFile):
    __tdlib_type__ = "datedFile"
    file: file = attr.ib()
    date: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deepLinkInfo(DeepLinkInfo):
    __tdlib_type__ = "deepLinkInfo"
    text: formattedText = attr.ib()
    need_update_application: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deviceTokenApplePush(DeviceToken):
    __tdlib_type__ = "deviceTokenApplePush"
    device_token: str = attr.ib()
    is_app_sandbox: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deviceTokenApplePushVoIP(DeviceToken):
    __tdlib_type__ = "deviceTokenApplePushVoIP"
    device_token: str = attr.ib()
    is_app_sandbox: bool = attr.ib()
    encrypt: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deviceTokenBlackBerryPush(DeviceToken):
    __tdlib_type__ = "deviceTokenBlackBerryPush"
    token: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deviceTokenFirebaseCloudMessaging(DeviceToken):
    __tdlib_type__ = "deviceTokenFirebaseCloudMessaging"
    token: str = attr.ib()
    encrypt: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deviceTokenMicrosoftPush(DeviceToken):
    __tdlib_type__ = "deviceTokenMicrosoftPush"
    channel_uri: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deviceTokenMicrosoftPushVoIP(DeviceToken):
    __tdlib_type__ = "deviceTokenMicrosoftPushVoIP"
    channel_uri: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deviceTokenSimplePush(DeviceToken):
    __tdlib_type__ = "deviceTokenSimplePush"
    endpoint: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deviceTokenTizenPush(DeviceToken):
    __tdlib_type__ = "deviceTokenTizenPush"
    reg_id: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deviceTokenUbuntuPush(DeviceToken):
    __tdlib_type__ = "deviceTokenUbuntuPush"
    token: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deviceTokenWebPush(DeviceToken):
    __tdlib_type__ = "deviceTokenWebPush"
    endpoint: str = attr.ib()
    p256dh_base64url: str = attr.ib()
    auth_base64url: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deviceTokenWindowsPush(DeviceToken):
    __tdlib_type__ = "deviceTokenWindowsPush"
    access_token: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class document(Document):
    __tdlib_type__ = "document"
    file_name: str = attr.ib()
    mime_type: str = attr.ib()
    minithumbnail: minithumbnail = attr.ib()
    thumbnail: photoSize = attr.ib()
    document: file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class draftMessage(DraftMessage):
    __tdlib_type__ = "draftMessage"
    reply_to_message_id: int = attr.ib()
    input_message_text: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class emailAddressAuthenticationCodeInfo(EmailAddressAuthenticationCodeInfo):
    __tdlib_type__ = "emailAddressAuthenticationCodeInfo"
    email_address_pattern: str = attr.ib()
    length: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class emojis(Emojis):
    __tdlib_type__ = "emojis"
    emojis: typing.Sequence[str] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class encryptedCredentials(EncryptedCredentials):
    __tdlib_type__ = "encryptedCredentials"
    data: bytes = attr.ib()
    hash: bytes = attr.ib()
    secret: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class encryptedPassportElement(EncryptedPassportElement):
    __tdlib_type__ = "encryptedPassportElement"
    type: PassportElementType = attr.ib()
    data: bytes = attr.ib()
    front_side: datedFile = attr.ib()
    reverse_side: datedFile = attr.ib()
    selfie: datedFile = attr.ib()
    translation: typing.Sequence[datedFile] = attr.ib()
    files: typing.Sequence[datedFile] = attr.ib()
    value: str = attr.ib()
    hash: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class error(Error):
    __tdlib_type__ = "error"
    code: int = attr.ib()
    message: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class file(File):
    __tdlib_type__ = "file"
    id: int = attr.ib()
    size: int = attr.ib()
    expected_size: int = attr.ib()
    local: localFile = attr.ib()
    remote: remoteFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class filePart(FilePart):
    __tdlib_type__ = "filePart"
    data: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeAnimation(FileType):
    __tdlib_type__ = "fileTypeAnimation"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeAudio(FileType):
    __tdlib_type__ = "fileTypeAudio"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeDocument(FileType):
    __tdlib_type__ = "fileTypeDocument"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeNone(FileType):
    __tdlib_type__ = "fileTypeNone"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypePhoto(FileType):
    __tdlib_type__ = "fileTypePhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeProfilePhoto(FileType):
    __tdlib_type__ = "fileTypeProfilePhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeSecret(FileType):
    __tdlib_type__ = "fileTypeSecret"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeSecretThumbnail(FileType):
    __tdlib_type__ = "fileTypeSecretThumbnail"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeSecure(FileType):
    __tdlib_type__ = "fileTypeSecure"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeSticker(FileType):
    __tdlib_type__ = "fileTypeSticker"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeThumbnail(FileType):
    __tdlib_type__ = "fileTypeThumbnail"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeUnknown(FileType):
    __tdlib_type__ = "fileTypeUnknown"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeVideo(FileType):
    __tdlib_type__ = "fileTypeVideo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeVideoNote(FileType):
    __tdlib_type__ = "fileTypeVideoNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeVoiceNote(FileType):
    __tdlib_type__ = "fileTypeVoiceNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class fileTypeWallpaper(FileType):
    __tdlib_type__ = "fileTypeWallpaper"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class formattedText(FormattedText):
    __tdlib_type__ = "formattedText"
    text: str = attr.ib()
    entities: typing.Sequence[textEntity] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class foundMessages(FoundMessages):
    __tdlib_type__ = "foundMessages"
    messages: typing.Sequence[message] = attr.ib()
    next_from_search_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class game(Game):
    __tdlib_type__ = "game"
    id: int = attr.ib()
    short_name: str = attr.ib()
    title: str = attr.ib()
    text: formattedText = attr.ib()
    description: str = attr.ib()
    photo: photo = attr.ib()
    animation: animation = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class gameHighScore(GameHighScore):
    __tdlib_type__ = "gameHighScore"
    position: int = attr.ib()
    user_id: int = attr.ib()
    score: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class gameHighScores(GameHighScores):
    __tdlib_type__ = "gameHighScores"
    scores: typing.Sequence[gameHighScore] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class hashtags(Hashtags):
    __tdlib_type__ = "hashtags"
    hashtags: typing.Sequence[str] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class httpUrl(HttpUrl):
    __tdlib_type__ = "httpUrl"
    url: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class identityDocument(IdentityDocument):
    __tdlib_type__ = "identityDocument"
    number: str = attr.ib()
    expiry_date: date = attr.ib()
    front_side: datedFile = attr.ib()
    reverse_side: datedFile = attr.ib()
    selfie: datedFile = attr.ib()
    translation: typing.Sequence[datedFile] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class importedContacts(ImportedContacts):
    __tdlib_type__ = "importedContacts"
    user_ids: typing.Sequence[int] = attr.ib()
    importer_count: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineKeyboardButton(InlineKeyboardButton):
    __tdlib_type__ = "inlineKeyboardButton"
    text: str = attr.ib()
    type: InlineKeyboardButtonType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineKeyboardButtonTypeBuy(InlineKeyboardButtonType):
    __tdlib_type__ = "inlineKeyboardButtonTypeBuy"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineKeyboardButtonTypeCallback(InlineKeyboardButtonType):
    __tdlib_type__ = "inlineKeyboardButtonTypeCallback"
    data: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineKeyboardButtonTypeCallbackGame(InlineKeyboardButtonType):
    __tdlib_type__ = "inlineKeyboardButtonTypeCallbackGame"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineKeyboardButtonTypeLoginUrl(InlineKeyboardButtonType):
    __tdlib_type__ = "inlineKeyboardButtonTypeLoginUrl"
    url: str = attr.ib()
    id: int = attr.ib()
    forward_text: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineKeyboardButtonTypeSwitchInline(InlineKeyboardButtonType):
    __tdlib_type__ = "inlineKeyboardButtonTypeSwitchInline"
    query: str = attr.ib()
    in_current_chat: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineKeyboardButtonTypeUrl(InlineKeyboardButtonType):
    __tdlib_type__ = "inlineKeyboardButtonTypeUrl"
    url: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineQueryResultAnimation(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultAnimation"
    id: str = attr.ib()
    animation: animation = attr.ib()
    title: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineQueryResultArticle(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultArticle"
    id: str = attr.ib()
    url: str = attr.ib()
    hide_url: bool = attr.ib()
    title: str = attr.ib()
    description: str = attr.ib()
    thumbnail: photoSize = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineQueryResultAudio(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultAudio"
    id: str = attr.ib()
    audio: audio = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineQueryResultContact(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultContact"
    id: str = attr.ib()
    contact: contact = attr.ib()
    thumbnail: photoSize = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineQueryResultDocument(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultDocument"
    id: str = attr.ib()
    document: document = attr.ib()
    title: str = attr.ib()
    description: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineQueryResultGame(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultGame"
    id: str = attr.ib()
    game: game = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineQueryResultLocation(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultLocation"
    id: str = attr.ib()
    location: location = attr.ib()
    title: str = attr.ib()
    thumbnail: photoSize = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineQueryResultPhoto(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultPhoto"
    id: str = attr.ib()
    photo: photo = attr.ib()
    title: str = attr.ib()
    description: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineQueryResultSticker(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultSticker"
    id: str = attr.ib()
    sticker: sticker = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineQueryResultVenue(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultVenue"
    id: str = attr.ib()
    venue: venue = attr.ib()
    thumbnail: photoSize = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineQueryResultVideo(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultVideo"
    id: str = attr.ib()
    video: video = attr.ib()
    title: str = attr.ib()
    description: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineQueryResultVoiceNote(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultVoiceNote"
    id: str = attr.ib()
    voice_note: voiceNote = attr.ib()
    title: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inlineQueryResults(InlineQueryResults):
    __tdlib_type__ = "inlineQueryResults"
    inline_query_id: int = attr.ib()
    next_offset: str = attr.ib()
    results: typing.Sequence[InlineQueryResult] = attr.ib()
    switch_pm_text: str = attr.ib()
    switch_pm_parameter: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputBackgroundLocal(InputBackground):
    __tdlib_type__ = "inputBackgroundLocal"
    background: InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputBackgroundRemote(InputBackground):
    __tdlib_type__ = "inputBackgroundRemote"
    background_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputCredentialsAndroidPay(InputCredentials):
    __tdlib_type__ = "inputCredentialsAndroidPay"
    data: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputCredentialsApplePay(InputCredentials):
    __tdlib_type__ = "inputCredentialsApplePay"
    data: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputCredentialsNew(InputCredentials):
    __tdlib_type__ = "inputCredentialsNew"
    data: str = attr.ib()
    allow_save: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputCredentialsSaved(InputCredentials):
    __tdlib_type__ = "inputCredentialsSaved"
    saved_credentials_id: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputFileGenerated(InputFile):
    __tdlib_type__ = "inputFileGenerated"
    original_path: str = attr.ib()
    conversion: str = attr.ib()
    expected_size: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputFileId(InputFile):
    __tdlib_type__ = "inputFileId"
    id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputFileLocal(InputFile):
    __tdlib_type__ = "inputFileLocal"
    path: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputFileRemote(InputFile):
    __tdlib_type__ = "inputFileRemote"
    id: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputIdentityDocument(InputIdentityDocument):
    __tdlib_type__ = "inputIdentityDocument"
    number: str = attr.ib()
    expiry_date: date = attr.ib()
    front_side: InputFile = attr.ib()
    reverse_side: InputFile = attr.ib()
    selfie: InputFile = attr.ib()
    translation: typing.Sequence[InputFile] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputInlineQueryResultAnimatedGif(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultAnimatedGif"
    id: str = attr.ib()
    title: str = attr.ib()
    thumbnail_url: str = attr.ib()
    gif_url: str = attr.ib()
    gif_duration: int = attr.ib()
    gif_width: int = attr.ib()
    gif_height: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputInlineQueryResultAnimatedMpeg4(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultAnimatedMpeg4"
    id: str = attr.ib()
    title: str = attr.ib()
    thumbnail_url: str = attr.ib()
    mpeg4_url: str = attr.ib()
    mpeg4_duration: int = attr.ib()
    mpeg4_width: int = attr.ib()
    mpeg4_height: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputInlineQueryResultArticle(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultArticle"
    id: str = attr.ib()
    url: str = attr.ib()
    hide_url: bool = attr.ib()
    title: str = attr.ib()
    description: str = attr.ib()
    thumbnail_url: str = attr.ib()
    thumbnail_width: int = attr.ib()
    thumbnail_height: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputInlineQueryResultAudio(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultAudio"
    id: str = attr.ib()
    title: str = attr.ib()
    performer: str = attr.ib()
    audio_url: str = attr.ib()
    audio_duration: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputInlineQueryResultContact(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultContact"
    id: str = attr.ib()
    contact: contact = attr.ib()
    thumbnail_url: str = attr.ib()
    thumbnail_width: int = attr.ib()
    thumbnail_height: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputInlineQueryResultDocument(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultDocument"
    id: str = attr.ib()
    title: str = attr.ib()
    description: str = attr.ib()
    document_url: str = attr.ib()
    mime_type: str = attr.ib()
    thumbnail_url: str = attr.ib()
    thumbnail_width: int = attr.ib()
    thumbnail_height: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputInlineQueryResultGame(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultGame"
    id: str = attr.ib()
    game_short_name: str = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputInlineQueryResultLocation(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultLocation"
    id: str = attr.ib()
    location: location = attr.ib()
    live_period: int = attr.ib()
    title: str = attr.ib()
    thumbnail_url: str = attr.ib()
    thumbnail_width: int = attr.ib()
    thumbnail_height: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputInlineQueryResultPhoto(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultPhoto"
    id: str = attr.ib()
    title: str = attr.ib()
    description: str = attr.ib()
    thumbnail_url: str = attr.ib()
    photo_url: str = attr.ib()
    photo_width: int = attr.ib()
    photo_height: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputInlineQueryResultSticker(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultSticker"
    id: str = attr.ib()
    thumbnail_url: str = attr.ib()
    sticker_url: str = attr.ib()
    sticker_width: int = attr.ib()
    sticker_height: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputInlineQueryResultVenue(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultVenue"
    id: str = attr.ib()
    venue: venue = attr.ib()
    thumbnail_url: str = attr.ib()
    thumbnail_width: int = attr.ib()
    thumbnail_height: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputInlineQueryResultVideo(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultVideo"
    id: str = attr.ib()
    title: str = attr.ib()
    description: str = attr.ib()
    thumbnail_url: str = attr.ib()
    video_url: str = attr.ib()
    mime_type: str = attr.ib()
    video_width: int = attr.ib()
    video_height: int = attr.ib()
    video_duration: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputInlineQueryResultVoiceNote(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultVoiceNote"
    id: str = attr.ib()
    title: str = attr.ib()
    voice_note_url: str = attr.ib()
    voice_note_duration: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessageAnimation(InputMessageContent):
    __tdlib_type__ = "inputMessageAnimation"
    animation: InputFile = attr.ib()
    thumbnail: inputThumbnail = attr.ib()
    duration: int = attr.ib()
    width: int = attr.ib()
    height: int = attr.ib()
    caption: formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessageAudio(InputMessageContent):
    __tdlib_type__ = "inputMessageAudio"
    audio: InputFile = attr.ib()
    album_cover_thumbnail: inputThumbnail = attr.ib()
    duration: int = attr.ib()
    title: str = attr.ib()
    performer: str = attr.ib()
    caption: formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessageContact(InputMessageContent):
    __tdlib_type__ = "inputMessageContact"
    contact: contact = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessageDocument(InputMessageContent):
    __tdlib_type__ = "inputMessageDocument"
    document: InputFile = attr.ib()
    thumbnail: inputThumbnail = attr.ib()
    caption: formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessageForwarded(InputMessageContent):
    __tdlib_type__ = "inputMessageForwarded"
    from_chat_id: int = attr.ib()
    message_id: int = attr.ib()
    in_game_share: bool = attr.ib()
    send_copy: bool = attr.ib()
    remove_caption: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessageGame(InputMessageContent):
    __tdlib_type__ = "inputMessageGame"
    bot_user_id: int = attr.ib()
    game_short_name: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessageInvoice(InputMessageContent):
    __tdlib_type__ = "inputMessageInvoice"
    invoice: invoice = attr.ib()
    title: str = attr.ib()
    description: str = attr.ib()
    photo_url: str = attr.ib()
    photo_size: int = attr.ib()
    photo_width: int = attr.ib()
    photo_height: int = attr.ib()
    payload: bytes = attr.ib()
    provider_token: str = attr.ib()
    provider_data: str = attr.ib()
    start_parameter: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessageLocation(InputMessageContent):
    __tdlib_type__ = "inputMessageLocation"
    location: location = attr.ib()
    live_period: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessagePhoto(InputMessageContent):
    __tdlib_type__ = "inputMessagePhoto"
    photo: InputFile = attr.ib()
    thumbnail: inputThumbnail = attr.ib()
    added_sticker_file_ids: typing.Sequence[int] = attr.ib()
    width: int = attr.ib()
    height: int = attr.ib()
    caption: formattedText = attr.ib()
    ttl: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessagePoll(InputMessageContent):
    __tdlib_type__ = "inputMessagePoll"
    question: str = attr.ib()
    options: typing.Sequence[str] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessageSticker(InputMessageContent):
    __tdlib_type__ = "inputMessageSticker"
    sticker: InputFile = attr.ib()
    thumbnail: inputThumbnail = attr.ib()
    width: int = attr.ib()
    height: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessageText(InputMessageContent):
    __tdlib_type__ = "inputMessageText"
    text: formattedText = attr.ib()
    disable_web_page_preview: bool = attr.ib()
    clear_draft: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessageVenue(InputMessageContent):
    __tdlib_type__ = "inputMessageVenue"
    venue: venue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessageVideo(InputMessageContent):
    __tdlib_type__ = "inputMessageVideo"
    video: InputFile = attr.ib()
    thumbnail: inputThumbnail = attr.ib()
    added_sticker_file_ids: typing.Sequence[int] = attr.ib()
    duration: int = attr.ib()
    width: int = attr.ib()
    height: int = attr.ib()
    supports_streaming: bool = attr.ib()
    caption: formattedText = attr.ib()
    ttl: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessageVideoNote(InputMessageContent):
    __tdlib_type__ = "inputMessageVideoNote"
    video_note: InputFile = attr.ib()
    thumbnail: inputThumbnail = attr.ib()
    duration: int = attr.ib()
    length: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputMessageVoiceNote(InputMessageContent):
    __tdlib_type__ = "inputMessageVoiceNote"
    voice_note: InputFile = attr.ib()
    duration: int = attr.ib()
    waveform: bytes = attr.ib()
    caption: formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementAddress(InputPassportElement):
    __tdlib_type__ = "inputPassportElementAddress"
    address: address = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementBankStatement(InputPassportElement):
    __tdlib_type__ = "inputPassportElementBankStatement"
    bank_statement: inputPersonalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementDriverLicense(InputPassportElement):
    __tdlib_type__ = "inputPassportElementDriverLicense"
    driver_license: inputIdentityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementEmailAddress(InputPassportElement):
    __tdlib_type__ = "inputPassportElementEmailAddress"
    email_address: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementError(InputPassportElementError):
    __tdlib_type__ = "inputPassportElementError"
    type: PassportElementType = attr.ib()
    message: str = attr.ib()
    source: InputPassportElementErrorSource = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementErrorSourceDataField(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceDataField"
    field_name: str = attr.ib()
    data_hash: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementErrorSourceFile(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceFile"
    file_hash: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementErrorSourceFiles(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceFiles"
    file_hashes: typing.Sequence[bytes] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementErrorSourceFrontSide(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceFrontSide"
    file_hash: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementErrorSourceReverseSide(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceReverseSide"
    file_hash: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementErrorSourceSelfie(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceSelfie"
    file_hash: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementErrorSourceTranslationFile(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceTranslationFile"
    file_hash: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementErrorSourceTranslationFiles(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceTranslationFiles"
    file_hashes: typing.Sequence[bytes] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementErrorSourceUnspecified(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceUnspecified"
    element_hash: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementIdentityCard(InputPassportElement):
    __tdlib_type__ = "inputPassportElementIdentityCard"
    identity_card: inputIdentityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementInternalPassport(InputPassportElement):
    __tdlib_type__ = "inputPassportElementInternalPassport"
    internal_passport: inputIdentityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementPassport(InputPassportElement):
    __tdlib_type__ = "inputPassportElementPassport"
    passport: inputIdentityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementPassportRegistration(InputPassportElement):
    __tdlib_type__ = "inputPassportElementPassportRegistration"
    passport_registration: inputPersonalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementPersonalDetails(InputPassportElement):
    __tdlib_type__ = "inputPassportElementPersonalDetails"
    personal_details: personalDetails = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementPhoneNumber(InputPassportElement):
    __tdlib_type__ = "inputPassportElementPhoneNumber"
    phone_number: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementRentalAgreement(InputPassportElement):
    __tdlib_type__ = "inputPassportElementRentalAgreement"
    rental_agreement: inputPersonalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementTemporaryRegistration(InputPassportElement):
    __tdlib_type__ = "inputPassportElementTemporaryRegistration"
    temporary_registration: inputPersonalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPassportElementUtilityBill(InputPassportElement):
    __tdlib_type__ = "inputPassportElementUtilityBill"
    utility_bill: inputPersonalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputPersonalDocument(InputPersonalDocument):
    __tdlib_type__ = "inputPersonalDocument"
    files: typing.Sequence[InputFile] = attr.ib()
    translation: typing.Sequence[InputFile] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputSticker(InputSticker):
    __tdlib_type__ = "inputSticker"
    png_sticker: InputFile = attr.ib()
    emojis: str = attr.ib()
    mask_position: maskPosition = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class inputThumbnail(InputThumbnail):
    __tdlib_type__ = "inputThumbnail"
    thumbnail: InputFile = attr.ib()
    width: int = attr.ib()
    height: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class invoice(Invoice):
    __tdlib_type__ = "invoice"
    currency: str = attr.ib()
    price_parts: typing.Sequence[labeledPricePart] = attr.ib()
    is_test: bool = attr.ib()
    need_name: bool = attr.ib()
    need_phone_number: bool = attr.ib()
    need_email_address: bool = attr.ib()
    need_shipping_address: bool = attr.ib()
    send_phone_number_to_provider: bool = attr.ib()
    send_email_address_to_provider: bool = attr.ib()
    is_flexible: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class jsonObjectMember(JsonObjectMember):
    __tdlib_type__ = "jsonObjectMember"
    key: str = attr.ib()
    value: JsonValue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class jsonValueArray(JsonValue):
    __tdlib_type__ = "jsonValueArray"
    values: typing.Sequence[JsonValue] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class jsonValueBoolean(JsonValue):
    __tdlib_type__ = "jsonValueBoolean"
    value: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class jsonValueNull(JsonValue):
    __tdlib_type__ = "jsonValueNull"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class jsonValueNumber(JsonValue):
    __tdlib_type__ = "jsonValueNumber"
    value: decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class jsonValueObject(JsonValue):
    __tdlib_type__ = "jsonValueObject"
    members: typing.Sequence[jsonObjectMember] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class jsonValueString(JsonValue):
    __tdlib_type__ = "jsonValueString"
    value: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class keyboardButton(KeyboardButton):
    __tdlib_type__ = "keyboardButton"
    text: str = attr.ib()
    type: KeyboardButtonType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class keyboardButtonTypeRequestLocation(KeyboardButtonType):
    __tdlib_type__ = "keyboardButtonTypeRequestLocation"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class keyboardButtonTypeRequestPhoneNumber(KeyboardButtonType):
    __tdlib_type__ = "keyboardButtonTypeRequestPhoneNumber"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class keyboardButtonTypeText(KeyboardButtonType):
    __tdlib_type__ = "keyboardButtonTypeText"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class labeledPricePart(LabeledPricePart):
    __tdlib_type__ = "labeledPricePart"
    label: str = attr.ib()
    amount: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class languagePackInfo(LanguagePackInfo):
    __tdlib_type__ = "languagePackInfo"
    id: str = attr.ib()
    base_language_pack_id: str = attr.ib()
    name: str = attr.ib()
    native_name: str = attr.ib()
    plural_code: str = attr.ib()
    is_official: bool = attr.ib()
    is_rtl: bool = attr.ib()
    is_beta: bool = attr.ib()
    is_installed: bool = attr.ib()
    total_string_count: int = attr.ib()
    translated_string_count: int = attr.ib()
    local_string_count: int = attr.ib()
    translation_url: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class languagePackString(LanguagePackString):
    __tdlib_type__ = "languagePackString"
    key: str = attr.ib()
    value: LanguagePackStringValue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class languagePackStringValueDeleted(LanguagePackStringValue):
    __tdlib_type__ = "languagePackStringValueDeleted"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class languagePackStringValueOrdinary(LanguagePackStringValue):
    __tdlib_type__ = "languagePackStringValueOrdinary"
    value: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class languagePackStringValuePluralized(LanguagePackStringValue):
    __tdlib_type__ = "languagePackStringValuePluralized"
    zero_value: str = attr.ib()
    one_value: str = attr.ib()
    two_value: str = attr.ib()
    few_value: str = attr.ib()
    many_value: str = attr.ib()
    other_value: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class languagePackStrings(LanguagePackStrings):
    __tdlib_type__ = "languagePackStrings"
    strings: typing.Sequence[languagePackString] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class localFile(LocalFile):
    __tdlib_type__ = "localFile"
    path: str = attr.ib()
    can_be_downloaded: bool = attr.ib()
    can_be_deleted: bool = attr.ib()
    is_downloading_active: bool = attr.ib()
    is_downloading_completed: bool = attr.ib()
    download_offset: int = attr.ib()
    downloaded_prefix_size: int = attr.ib()
    downloaded_size: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class localizationTargetInfo(LocalizationTargetInfo):
    __tdlib_type__ = "localizationTargetInfo"
    language_packs: typing.Sequence[languagePackInfo] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class location(Location):
    __tdlib_type__ = "location"
    latitude: decimal.Decimal = attr.ib()
    longitude: decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class logStreamDefault(LogStream):
    __tdlib_type__ = "logStreamDefault"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class logStreamEmpty(LogStream):
    __tdlib_type__ = "logStreamEmpty"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class logStreamFile(LogStream):
    __tdlib_type__ = "logStreamFile"
    path: str = attr.ib()
    max_file_size: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class logTags(LogTags):
    __tdlib_type__ = "logTags"
    tags: typing.Sequence[str] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class logVerbosityLevel(LogVerbosityLevel):
    __tdlib_type__ = "logVerbosityLevel"
    verbosity_level: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class loginUrlInfoOpen(LoginUrlInfo):
    __tdlib_type__ = "loginUrlInfoOpen"
    url: str = attr.ib()
    skip_confirm: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class loginUrlInfoRequestConfirmation(LoginUrlInfo):
    __tdlib_type__ = "loginUrlInfoRequestConfirmation"
    url: str = attr.ib()
    domain: str = attr.ib()
    bot_user_id: int = attr.ib()
    request_write_access: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class maskPointChin(MaskPoint):
    __tdlib_type__ = "maskPointChin"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class maskPointEyes(MaskPoint):
    __tdlib_type__ = "maskPointEyes"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class maskPointForehead(MaskPoint):
    __tdlib_type__ = "maskPointForehead"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class maskPointMouth(MaskPoint):
    __tdlib_type__ = "maskPointMouth"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class maskPosition(MaskPosition):
    __tdlib_type__ = "maskPosition"
    point: MaskPoint = attr.ib()
    x_shift: decimal.Decimal = attr.ib()
    y_shift: decimal.Decimal = attr.ib()
    scale: decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class message(Message):
    __tdlib_type__ = "message"
    id: int = attr.ib()
    sender_user_id: int = attr.ib()
    chat_id: int = attr.ib()
    sending_state: MessageSendingState = attr.ib()
    scheduling_state: MessageSchedulingState = attr.ib()
    is_outgoing: bool = attr.ib()
    can_be_edited: bool = attr.ib()
    can_be_forwarded: bool = attr.ib()
    can_be_deleted_only_for_self: bool = attr.ib()
    can_be_deleted_for_all_users: bool = attr.ib()
    is_channel_post: bool = attr.ib()
    contains_unread_mention: bool = attr.ib()
    date: int = attr.ib()
    edit_date: int = attr.ib()
    forward_info: messageForwardInfo = attr.ib()
    reply_to_message_id: int = attr.ib()
    ttl: int = attr.ib()
    ttl_expires_in: decimal.Decimal = attr.ib()
    via_bot_user_id: int = attr.ib()
    author_signature: str = attr.ib()
    views: int = attr.ib()
    media_album_id: int = attr.ib()
    restriction_reason: str = attr.ib()
    content: MessageContent = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageAnimation(MessageContent):
    __tdlib_type__ = "messageAnimation"
    animation: animation = attr.ib()
    caption: formattedText = attr.ib()
    is_secret: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageAudio(MessageContent):
    __tdlib_type__ = "messageAudio"
    audio: audio = attr.ib()
    caption: formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageBasicGroupChatCreate(MessageContent):
    __tdlib_type__ = "messageBasicGroupChatCreate"
    title: str = attr.ib()
    member_user_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageCall(MessageContent):
    __tdlib_type__ = "messageCall"
    discard_reason: CallDiscardReason = attr.ib()
    duration: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageChatAddMembers(MessageContent):
    __tdlib_type__ = "messageChatAddMembers"
    member_user_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageChatChangePhoto(MessageContent):
    __tdlib_type__ = "messageChatChangePhoto"
    photo: photo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageChatChangeTitle(MessageContent):
    __tdlib_type__ = "messageChatChangeTitle"
    title: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageChatDeleteMember(MessageContent):
    __tdlib_type__ = "messageChatDeleteMember"
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageChatDeletePhoto(MessageContent):
    __tdlib_type__ = "messageChatDeletePhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageChatJoinByLink(MessageContent):
    __tdlib_type__ = "messageChatJoinByLink"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageChatSetTtl(MessageContent):
    __tdlib_type__ = "messageChatSetTtl"
    ttl: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageChatUpgradeFrom(MessageContent):
    __tdlib_type__ = "messageChatUpgradeFrom"
    title: str = attr.ib()
    basic_group_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageChatUpgradeTo(MessageContent):
    __tdlib_type__ = "messageChatUpgradeTo"
    supergroup_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageContact(MessageContent):
    __tdlib_type__ = "messageContact"
    contact: contact = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageContactRegistered(MessageContent):
    __tdlib_type__ = "messageContactRegistered"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageCustomServiceAction(MessageContent):
    __tdlib_type__ = "messageCustomServiceAction"
    text: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageDocument(MessageContent):
    __tdlib_type__ = "messageDocument"
    document: document = attr.ib()
    caption: formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageExpiredPhoto(MessageContent):
    __tdlib_type__ = "messageExpiredPhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageExpiredVideo(MessageContent):
    __tdlib_type__ = "messageExpiredVideo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageForwardInfo(MessageForwardInfo):
    __tdlib_type__ = "messageForwardInfo"
    origin: MessageForwardOrigin = attr.ib()
    date: int = attr.ib()
    from_chat_id: int = attr.ib()
    from_message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageForwardOriginChannel(MessageForwardOrigin):
    __tdlib_type__ = "messageForwardOriginChannel"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    author_signature: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageForwardOriginHiddenUser(MessageForwardOrigin):
    __tdlib_type__ = "messageForwardOriginHiddenUser"
    sender_name: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageForwardOriginUser(MessageForwardOrigin):
    __tdlib_type__ = "messageForwardOriginUser"
    sender_user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageGame(MessageContent):
    __tdlib_type__ = "messageGame"
    game: game = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageGameScore(MessageContent):
    __tdlib_type__ = "messageGameScore"
    game_message_id: int = attr.ib()
    game_id: int = attr.ib()
    score: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageInvoice(MessageContent):
    __tdlib_type__ = "messageInvoice"
    title: str = attr.ib()
    description: str = attr.ib()
    photo: photo = attr.ib()
    currency: str = attr.ib()
    total_amount: int = attr.ib()
    start_parameter: str = attr.ib()
    is_test: bool = attr.ib()
    need_shipping_address: bool = attr.ib()
    receipt_message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageLinkInfo(MessageLinkInfo):
    __tdlib_type__ = "messageLinkInfo"
    is_public: bool = attr.ib()
    chat_id: int = attr.ib()
    message: message = attr.ib()
    for_album: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageLocation(MessageContent):
    __tdlib_type__ = "messageLocation"
    location: location = attr.ib()
    live_period: int = attr.ib()
    expires_in: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messagePassportDataReceived(MessageContent):
    __tdlib_type__ = "messagePassportDataReceived"
    elements: typing.Sequence[encryptedPassportElement] = attr.ib()
    credentials: encryptedCredentials = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messagePassportDataSent(MessageContent):
    __tdlib_type__ = "messagePassportDataSent"
    types: typing.Sequence[PassportElementType] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messagePaymentSuccessful(MessageContent):
    __tdlib_type__ = "messagePaymentSuccessful"
    invoice_message_id: int = attr.ib()
    currency: str = attr.ib()
    total_amount: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messagePaymentSuccessfulBot(MessageContent):
    __tdlib_type__ = "messagePaymentSuccessfulBot"
    invoice_message_id: int = attr.ib()
    currency: str = attr.ib()
    total_amount: int = attr.ib()
    invoice_payload: bytes = attr.ib()
    shipping_option_id: str = attr.ib()
    order_info: orderInfo = attr.ib()
    telegram_payment_charge_id: str = attr.ib()
    provider_payment_charge_id: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messagePhoto(MessageContent):
    __tdlib_type__ = "messagePhoto"
    photo: photo = attr.ib()
    caption: formattedText = attr.ib()
    is_secret: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messagePinMessage(MessageContent):
    __tdlib_type__ = "messagePinMessage"
    message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messagePoll(MessageContent):
    __tdlib_type__ = "messagePoll"
    poll: poll = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageSchedulingStateSendAtDate(MessageSchedulingState):
    __tdlib_type__ = "messageSchedulingStateSendAtDate"
    send_date: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageSchedulingStateSendWhenOnline(MessageSchedulingState):
    __tdlib_type__ = "messageSchedulingStateSendWhenOnline"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageScreenshotTaken(MessageContent):
    __tdlib_type__ = "messageScreenshotTaken"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageSendingStateFailed(MessageSendingState):
    __tdlib_type__ = "messageSendingStateFailed"
    error_code: int = attr.ib()
    error_message: str = attr.ib()
    can_retry: bool = attr.ib()
    retry_after: decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageSendingStatePending(MessageSendingState):
    __tdlib_type__ = "messageSendingStatePending"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageSticker(MessageContent):
    __tdlib_type__ = "messageSticker"
    sticker: sticker = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageSupergroupChatCreate(MessageContent):
    __tdlib_type__ = "messageSupergroupChatCreate"
    title: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageText(MessageContent):
    __tdlib_type__ = "messageText"
    text: formattedText = attr.ib()
    web_page: webPage = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageUnsupported(MessageContent):
    __tdlib_type__ = "messageUnsupported"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageVenue(MessageContent):
    __tdlib_type__ = "messageVenue"
    venue: venue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageVideo(MessageContent):
    __tdlib_type__ = "messageVideo"
    video: video = attr.ib()
    caption: formattedText = attr.ib()
    is_secret: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageVideoNote(MessageContent):
    __tdlib_type__ = "messageVideoNote"
    video_note: videoNote = attr.ib()
    is_viewed: bool = attr.ib()
    is_secret: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageVoiceNote(MessageContent):
    __tdlib_type__ = "messageVoiceNote"
    voice_note: voiceNote = attr.ib()
    caption: formattedText = attr.ib()
    is_listened: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messageWebsiteConnected(MessageContent):
    __tdlib_type__ = "messageWebsiteConnected"
    domain_name: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class messages(Messages):
    __tdlib_type__ = "messages"
    total_count: int = attr.ib()
    messages: typing.Sequence[message] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class minithumbnail(Minithumbnail):
    __tdlib_type__ = "minithumbnail"
    width: int = attr.ib()
    height: int = attr.ib()
    data: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class networkStatistics(NetworkStatistics):
    __tdlib_type__ = "networkStatistics"
    since_date: int = attr.ib()
    entries: typing.Sequence[NetworkStatisticsEntry] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class networkStatisticsEntryCall(NetworkStatisticsEntry):
    __tdlib_type__ = "networkStatisticsEntryCall"
    network_type: NetworkType = attr.ib()
    sent_bytes: int = attr.ib()
    received_bytes: int = attr.ib()
    duration: decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class networkStatisticsEntryFile(NetworkStatisticsEntry):
    __tdlib_type__ = "networkStatisticsEntryFile"
    file_type: FileType = attr.ib()
    network_type: NetworkType = attr.ib()
    sent_bytes: int = attr.ib()
    received_bytes: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class networkTypeMobile(NetworkType):
    __tdlib_type__ = "networkTypeMobile"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class networkTypeMobileRoaming(NetworkType):
    __tdlib_type__ = "networkTypeMobileRoaming"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class networkTypeNone(NetworkType):
    __tdlib_type__ = "networkTypeNone"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class networkTypeOther(NetworkType):
    __tdlib_type__ = "networkTypeOther"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class networkTypeWiFi(NetworkType):
    __tdlib_type__ = "networkTypeWiFi"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class notification(Notification):
    __tdlib_type__ = "notification"
    id: int = attr.ib()
    date: int = attr.ib()
    is_silent: bool = attr.ib()
    type: NotificationType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class notificationGroup(NotificationGroup):
    __tdlib_type__ = "notificationGroup"
    id: int = attr.ib()
    type: NotificationGroupType = attr.ib()
    chat_id: int = attr.ib()
    total_count: int = attr.ib()
    notifications: typing.Sequence[notification] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class notificationGroupTypeCalls(NotificationGroupType):
    __tdlib_type__ = "notificationGroupTypeCalls"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class notificationGroupTypeMentions(NotificationGroupType):
    __tdlib_type__ = "notificationGroupTypeMentions"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class notificationGroupTypeMessages(NotificationGroupType):
    __tdlib_type__ = "notificationGroupTypeMessages"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class notificationGroupTypeSecretChat(NotificationGroupType):
    __tdlib_type__ = "notificationGroupTypeSecretChat"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class notificationSettingsScopeChannelChats(NotificationSettingsScope):
    __tdlib_type__ = "notificationSettingsScopeChannelChats"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class notificationSettingsScopeGroupChats(NotificationSettingsScope):
    __tdlib_type__ = "notificationSettingsScopeGroupChats"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class notificationSettingsScopePrivateChats(NotificationSettingsScope):
    __tdlib_type__ = "notificationSettingsScopePrivateChats"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class notificationTypeNewCall(NotificationType):
    __tdlib_type__ = "notificationTypeNewCall"
    call_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class notificationTypeNewMessage(NotificationType):
    __tdlib_type__ = "notificationTypeNewMessage"
    message: message = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class notificationTypeNewPushMessage(NotificationType):
    __tdlib_type__ = "notificationTypeNewPushMessage"
    message_id: int = attr.ib()
    sender_user_id: int = attr.ib()
    content: PushMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class notificationTypeNewSecretChat(NotificationType):
    __tdlib_type__ = "notificationTypeNewSecretChat"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ok(Ok):
    __tdlib_type__ = "ok"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class optionValueBoolean(OptionValue):
    __tdlib_type__ = "optionValueBoolean"
    value: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class optionValueEmpty(OptionValue):
    __tdlib_type__ = "optionValueEmpty"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class optionValueInteger(OptionValue):
    __tdlib_type__ = "optionValueInteger"
    value: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class optionValueString(OptionValue):
    __tdlib_type__ = "optionValueString"
    value: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class orderInfo(OrderInfo):
    __tdlib_type__ = "orderInfo"
    name: str = attr.ib()
    phone_number: str = attr.ib()
    email_address: str = attr.ib()
    shipping_address: address = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockAnchor(PageBlock):
    __tdlib_type__ = "pageBlockAnchor"
    name: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockAnimation(PageBlock):
    __tdlib_type__ = "pageBlockAnimation"
    animation: animation = attr.ib()
    caption: pageBlockCaption = attr.ib()
    need_autoplay: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockAudio(PageBlock):
    __tdlib_type__ = "pageBlockAudio"
    audio: audio = attr.ib()
    caption: pageBlockCaption = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockAuthorDate(PageBlock):
    __tdlib_type__ = "pageBlockAuthorDate"
    author: RichText = attr.ib()
    publish_date: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockBlockQuote(PageBlock):
    __tdlib_type__ = "pageBlockBlockQuote"
    text: RichText = attr.ib()
    credit: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockCaption(PageBlockCaption):
    __tdlib_type__ = "pageBlockCaption"
    text: RichText = attr.ib()
    credit: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockChatLink(PageBlock):
    __tdlib_type__ = "pageBlockChatLink"
    title: str = attr.ib()
    photo: chatPhoto = attr.ib()
    username: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockCollage(PageBlock):
    __tdlib_type__ = "pageBlockCollage"
    page_blocks: typing.Sequence[PageBlock] = attr.ib()
    caption: pageBlockCaption = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockCover(PageBlock):
    __tdlib_type__ = "pageBlockCover"
    cover: PageBlock = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockDetails(PageBlock):
    __tdlib_type__ = "pageBlockDetails"
    header: RichText = attr.ib()
    page_blocks: typing.Sequence[PageBlock] = attr.ib()
    is_open: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockDivider(PageBlock):
    __tdlib_type__ = "pageBlockDivider"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockEmbedded(PageBlock):
    __tdlib_type__ = "pageBlockEmbedded"
    url: str = attr.ib()
    html: str = attr.ib()
    poster_photo: photo = attr.ib()
    width: int = attr.ib()
    height: int = attr.ib()
    caption: pageBlockCaption = attr.ib()
    is_full_width: bool = attr.ib()
    allow_scrolling: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockEmbeddedPost(PageBlock):
    __tdlib_type__ = "pageBlockEmbeddedPost"
    url: str = attr.ib()
    author: str = attr.ib()
    author_photo: photo = attr.ib()
    date: int = attr.ib()
    page_blocks: typing.Sequence[PageBlock] = attr.ib()
    caption: pageBlockCaption = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockFooter(PageBlock):
    __tdlib_type__ = "pageBlockFooter"
    footer: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockHeader(PageBlock):
    __tdlib_type__ = "pageBlockHeader"
    header: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockHorizontalAlignmentCenter(PageBlockHorizontalAlignment):
    __tdlib_type__ = "pageBlockHorizontalAlignmentCenter"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockHorizontalAlignmentLeft(PageBlockHorizontalAlignment):
    __tdlib_type__ = "pageBlockHorizontalAlignmentLeft"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockHorizontalAlignmentRight(PageBlockHorizontalAlignment):
    __tdlib_type__ = "pageBlockHorizontalAlignmentRight"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockKicker(PageBlock):
    __tdlib_type__ = "pageBlockKicker"
    kicker: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockList(PageBlock):
    __tdlib_type__ = "pageBlockList"
    items: typing.Sequence[pageBlockListItem] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockListItem(PageBlockListItem):
    __tdlib_type__ = "pageBlockListItem"
    label: str = attr.ib()
    page_blocks: typing.Sequence[PageBlock] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockMap(PageBlock):
    __tdlib_type__ = "pageBlockMap"
    location: location = attr.ib()
    zoom: int = attr.ib()
    width: int = attr.ib()
    height: int = attr.ib()
    caption: pageBlockCaption = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockParagraph(PageBlock):
    __tdlib_type__ = "pageBlockParagraph"
    text: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockPhoto(PageBlock):
    __tdlib_type__ = "pageBlockPhoto"
    photo: photo = attr.ib()
    caption: pageBlockCaption = attr.ib()
    url: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockPreformatted(PageBlock):
    __tdlib_type__ = "pageBlockPreformatted"
    text: RichText = attr.ib()
    language: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockPullQuote(PageBlock):
    __tdlib_type__ = "pageBlockPullQuote"
    text: RichText = attr.ib()
    credit: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockRelatedArticle(PageBlockRelatedArticle):
    __tdlib_type__ = "pageBlockRelatedArticle"
    url: str = attr.ib()
    title: str = attr.ib()
    description: str = attr.ib()
    photo: photo = attr.ib()
    author: str = attr.ib()
    publish_date: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockRelatedArticles(PageBlock):
    __tdlib_type__ = "pageBlockRelatedArticles"
    header: RichText = attr.ib()
    articles: typing.Sequence[pageBlockRelatedArticle] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockSlideshow(PageBlock):
    __tdlib_type__ = "pageBlockSlideshow"
    page_blocks: typing.Sequence[PageBlock] = attr.ib()
    caption: pageBlockCaption = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockSubheader(PageBlock):
    __tdlib_type__ = "pageBlockSubheader"
    subheader: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockSubtitle(PageBlock):
    __tdlib_type__ = "pageBlockSubtitle"
    subtitle: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockTable(PageBlock):
    __tdlib_type__ = "pageBlockTable"
    caption: RichText = attr.ib()
    cells: typing.Sequence[typing.Sequence[pageBlockTableCell]] = attr.ib()
    is_bordered: bool = attr.ib()
    is_striped: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockTableCell(PageBlockTableCell):
    __tdlib_type__ = "pageBlockTableCell"
    text: RichText = attr.ib()
    is_header: bool = attr.ib()
    colspan: int = attr.ib()
    rowspan: int = attr.ib()
    align: PageBlockHorizontalAlignment = attr.ib()
    valign: PageBlockVerticalAlignment = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockTitle(PageBlock):
    __tdlib_type__ = "pageBlockTitle"
    title: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockVerticalAlignmentBottom(PageBlockVerticalAlignment):
    __tdlib_type__ = "pageBlockVerticalAlignmentBottom"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockVerticalAlignmentMiddle(PageBlockVerticalAlignment):
    __tdlib_type__ = "pageBlockVerticalAlignmentMiddle"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockVerticalAlignmentTop(PageBlockVerticalAlignment):
    __tdlib_type__ = "pageBlockVerticalAlignmentTop"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockVideo(PageBlock):
    __tdlib_type__ = "pageBlockVideo"
    video: video = attr.ib()
    caption: pageBlockCaption = attr.ib()
    need_autoplay: bool = attr.ib()
    is_looped: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pageBlockVoiceNote(PageBlock):
    __tdlib_type__ = "pageBlockVoiceNote"
    voice_note: voiceNote = attr.ib()
    caption: pageBlockCaption = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportAuthorizationForm(PassportAuthorizationForm):
    __tdlib_type__ = "passportAuthorizationForm"
    id: int = attr.ib()
    required_elements: typing.Sequence[passportRequiredElement] = attr.ib()
    privacy_policy_url: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementAddress(PassportElement):
    __tdlib_type__ = "passportElementAddress"
    address: address = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementBankStatement(PassportElement):
    __tdlib_type__ = "passportElementBankStatement"
    bank_statement: personalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementDriverLicense(PassportElement):
    __tdlib_type__ = "passportElementDriverLicense"
    driver_license: identityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementEmailAddress(PassportElement):
    __tdlib_type__ = "passportElementEmailAddress"
    email_address: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementError(PassportElementError):
    __tdlib_type__ = "passportElementError"
    type: PassportElementType = attr.ib()
    message: str = attr.ib()
    source: PassportElementErrorSource = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementErrorSourceDataField(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceDataField"
    field_name: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementErrorSourceFile(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceFile"
    file_index: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementErrorSourceFiles(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceFiles"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementErrorSourceFrontSide(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceFrontSide"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementErrorSourceReverseSide(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceReverseSide"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementErrorSourceSelfie(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceSelfie"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementErrorSourceTranslationFile(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceTranslationFile"
    file_index: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementErrorSourceTranslationFiles(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceTranslationFiles"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementErrorSourceUnspecified(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceUnspecified"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementIdentityCard(PassportElement):
    __tdlib_type__ = "passportElementIdentityCard"
    identity_card: identityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementInternalPassport(PassportElement):
    __tdlib_type__ = "passportElementInternalPassport"
    internal_passport: identityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementPassport(PassportElement):
    __tdlib_type__ = "passportElementPassport"
    passport: identityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementPassportRegistration(PassportElement):
    __tdlib_type__ = "passportElementPassportRegistration"
    passport_registration: personalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementPersonalDetails(PassportElement):
    __tdlib_type__ = "passportElementPersonalDetails"
    personal_details: personalDetails = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementPhoneNumber(PassportElement):
    __tdlib_type__ = "passportElementPhoneNumber"
    phone_number: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementRentalAgreement(PassportElement):
    __tdlib_type__ = "passportElementRentalAgreement"
    rental_agreement: personalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementTemporaryRegistration(PassportElement):
    __tdlib_type__ = "passportElementTemporaryRegistration"
    temporary_registration: personalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementTypeAddress(PassportElementType):
    __tdlib_type__ = "passportElementTypeAddress"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementTypeBankStatement(PassportElementType):
    __tdlib_type__ = "passportElementTypeBankStatement"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementTypeDriverLicense(PassportElementType):
    __tdlib_type__ = "passportElementTypeDriverLicense"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementTypeEmailAddress(PassportElementType):
    __tdlib_type__ = "passportElementTypeEmailAddress"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementTypeIdentityCard(PassportElementType):
    __tdlib_type__ = "passportElementTypeIdentityCard"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementTypeInternalPassport(PassportElementType):
    __tdlib_type__ = "passportElementTypeInternalPassport"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementTypePassport(PassportElementType):
    __tdlib_type__ = "passportElementTypePassport"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementTypePassportRegistration(PassportElementType):
    __tdlib_type__ = "passportElementTypePassportRegistration"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementTypePersonalDetails(PassportElementType):
    __tdlib_type__ = "passportElementTypePersonalDetails"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementTypePhoneNumber(PassportElementType):
    __tdlib_type__ = "passportElementTypePhoneNumber"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementTypeRentalAgreement(PassportElementType):
    __tdlib_type__ = "passportElementTypeRentalAgreement"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementTypeTemporaryRegistration(PassportElementType):
    __tdlib_type__ = "passportElementTypeTemporaryRegistration"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementTypeUtilityBill(PassportElementType):
    __tdlib_type__ = "passportElementTypeUtilityBill"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementUtilityBill(PassportElement):
    __tdlib_type__ = "passportElementUtilityBill"
    utility_bill: personalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElements(PassportElements):
    __tdlib_type__ = "passportElements"
    elements: typing.Sequence[PassportElement] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportElementsWithErrors(PassportElementsWithErrors):
    __tdlib_type__ = "passportElementsWithErrors"
    elements: typing.Sequence[PassportElement] = attr.ib()
    errors: typing.Sequence[passportElementError] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportRequiredElement(PassportRequiredElement):
    __tdlib_type__ = "passportRequiredElement"
    suitable_elements: typing.Sequence[passportSuitableElement] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passportSuitableElement(PassportSuitableElement):
    __tdlib_type__ = "passportSuitableElement"
    type: PassportElementType = attr.ib()
    is_selfie_required: bool = attr.ib()
    is_translation_required: bool = attr.ib()
    is_native_name_required: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class passwordState(PasswordState):
    __tdlib_type__ = "passwordState"
    has_password: bool = attr.ib()
    password_hint: str = attr.ib()
    has_recovery_email_address: bool = attr.ib()
    has_passport_data: bool = attr.ib()
    recovery_email_address_code_info: emailAddressAuthenticationCodeInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class paymentForm(PaymentForm):
    __tdlib_type__ = "paymentForm"
    invoice: invoice = attr.ib()
    url: str = attr.ib()
    payments_provider: paymentsProviderStripe = attr.ib()
    saved_order_info: orderInfo = attr.ib()
    saved_credentials: savedCredentials = attr.ib()
    can_save_credentials: bool = attr.ib()
    need_password: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class paymentReceipt(PaymentReceipt):
    __tdlib_type__ = "paymentReceipt"
    date: int = attr.ib()
    payments_provider_user_id: int = attr.ib()
    invoice: invoice = attr.ib()
    order_info: orderInfo = attr.ib()
    shipping_option: shippingOption = attr.ib()
    credentials_title: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class paymentResult(PaymentResult):
    __tdlib_type__ = "paymentResult"
    success: bool = attr.ib()
    verification_url: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class paymentsProviderStripe(PaymentsProviderStripe):
    __tdlib_type__ = "paymentsProviderStripe"
    publishable_key: str = attr.ib()
    need_country: bool = attr.ib()
    need_postal_code: bool = attr.ib()
    need_cardholder_name: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class personalDetails(PersonalDetails):
    __tdlib_type__ = "personalDetails"
    first_name: str = attr.ib()
    middle_name: str = attr.ib()
    last_name: str = attr.ib()
    native_first_name: str = attr.ib()
    native_middle_name: str = attr.ib()
    native_last_name: str = attr.ib()
    birthdate: date = attr.ib()
    gender: str = attr.ib()
    country_code: str = attr.ib()
    residence_country_code: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class personalDocument(PersonalDocument):
    __tdlib_type__ = "personalDocument"
    files: typing.Sequence[datedFile] = attr.ib()
    translation: typing.Sequence[datedFile] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class phoneNumberAuthenticationSettings(PhoneNumberAuthenticationSettings):
    __tdlib_type__ = "phoneNumberAuthenticationSettings"
    allow_flash_call: bool = attr.ib()
    is_current_phone_number: bool = attr.ib()
    allow_sms_retriever_api: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class photo(Photo):
    __tdlib_type__ = "photo"
    has_stickers: bool = attr.ib()
    minithumbnail: minithumbnail = attr.ib()
    sizes: typing.Sequence[photoSize] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class photoSize(PhotoSize):
    __tdlib_type__ = "photoSize"
    type: str = attr.ib()
    photo: file = attr.ib()
    width: int = attr.ib()
    height: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class poll(Poll):
    __tdlib_type__ = "poll"
    id: int = attr.ib()
    question: str = attr.ib()
    options: typing.Sequence[pollOption] = attr.ib()
    total_voter_count: int = attr.ib()
    is_closed: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pollOption(PollOption):
    __tdlib_type__ = "pollOption"
    text: str = attr.ib()
    voter_count: int = attr.ib()
    vote_percentage: int = attr.ib()
    is_chosen: bool = attr.ib()
    is_being_chosen: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class profilePhoto(ProfilePhoto):
    __tdlib_type__ = "profilePhoto"
    id: int = attr.ib()
    small: file = attr.ib()
    big: file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class proxies(Proxies):
    __tdlib_type__ = "proxies"
    proxies: typing.Sequence[proxy] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class proxy(Proxy):
    __tdlib_type__ = "proxy"
    id: int = attr.ib()
    server: str = attr.ib()
    port: int = attr.ib()
    last_used_date: int = attr.ib()
    is_enabled: bool = attr.ib()
    type: ProxyType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class proxyTypeHttp(ProxyType):
    __tdlib_type__ = "proxyTypeHttp"
    username: str = attr.ib()
    password: str = attr.ib()
    http_only: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class proxyTypeMtproto(ProxyType):
    __tdlib_type__ = "proxyTypeMtproto"
    secret: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class proxyTypeSocks5(ProxyType):
    __tdlib_type__ = "proxyTypeSocks5"
    username: str = attr.ib()
    password: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class publicChatTypeHasUsername(PublicChatType):
    __tdlib_type__ = "publicChatTypeHasUsername"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class publicChatTypeIsLocationBased(PublicChatType):
    __tdlib_type__ = "publicChatTypeIsLocationBased"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class publicMessageLink(PublicMessageLink):
    __tdlib_type__ = "publicMessageLink"
    link: str = attr.ib()
    html: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentAnimation(PushMessageContent):
    __tdlib_type__ = "pushMessageContentAnimation"
    animation: animation = attr.ib()
    caption: str = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentAudio(PushMessageContent):
    __tdlib_type__ = "pushMessageContentAudio"
    audio: audio = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentBasicGroupChatCreate(PushMessageContent):
    __tdlib_type__ = "pushMessageContentBasicGroupChatCreate"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentChatAddMembers(PushMessageContent):
    __tdlib_type__ = "pushMessageContentChatAddMembers"
    member_name: str = attr.ib()
    is_current_user: bool = attr.ib()
    is_returned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentChatChangePhoto(PushMessageContent):
    __tdlib_type__ = "pushMessageContentChatChangePhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentChatChangeTitle(PushMessageContent):
    __tdlib_type__ = "pushMessageContentChatChangeTitle"
    title: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentChatDeleteMember(PushMessageContent):
    __tdlib_type__ = "pushMessageContentChatDeleteMember"
    member_name: str = attr.ib()
    is_current_user: bool = attr.ib()
    is_left: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentChatJoinByLink(PushMessageContent):
    __tdlib_type__ = "pushMessageContentChatJoinByLink"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentContact(PushMessageContent):
    __tdlib_type__ = "pushMessageContentContact"
    name: str = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentContactRegistered(PushMessageContent):
    __tdlib_type__ = "pushMessageContentContactRegistered"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentDocument(PushMessageContent):
    __tdlib_type__ = "pushMessageContentDocument"
    document: document = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentGame(PushMessageContent):
    __tdlib_type__ = "pushMessageContentGame"
    title: str = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentGameScore(PushMessageContent):
    __tdlib_type__ = "pushMessageContentGameScore"
    title: str = attr.ib()
    score: int = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentHidden(PushMessageContent):
    __tdlib_type__ = "pushMessageContentHidden"
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentInvoice(PushMessageContent):
    __tdlib_type__ = "pushMessageContentInvoice"
    price: str = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentLocation(PushMessageContent):
    __tdlib_type__ = "pushMessageContentLocation"
    is_live: bool = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentMediaAlbum(PushMessageContent):
    __tdlib_type__ = "pushMessageContentMediaAlbum"
    total_count: int = attr.ib()
    has_photos: bool = attr.ib()
    has_videos: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentMessageForwards(PushMessageContent):
    __tdlib_type__ = "pushMessageContentMessageForwards"
    total_count: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentPhoto(PushMessageContent):
    __tdlib_type__ = "pushMessageContentPhoto"
    photo: photo = attr.ib()
    caption: str = attr.ib()
    is_secret: bool = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentPoll(PushMessageContent):
    __tdlib_type__ = "pushMessageContentPoll"
    question: str = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentScreenshotTaken(PushMessageContent):
    __tdlib_type__ = "pushMessageContentScreenshotTaken"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentSticker(PushMessageContent):
    __tdlib_type__ = "pushMessageContentSticker"
    sticker: sticker = attr.ib()
    emoji: str = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentText(PushMessageContent):
    __tdlib_type__ = "pushMessageContentText"
    text: str = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentVideo(PushMessageContent):
    __tdlib_type__ = "pushMessageContentVideo"
    video: video = attr.ib()
    caption: str = attr.ib()
    is_secret: bool = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentVideoNote(PushMessageContent):
    __tdlib_type__ = "pushMessageContentVideoNote"
    video_note: videoNote = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushMessageContentVoiceNote(PushMessageContent):
    __tdlib_type__ = "pushMessageContentVoiceNote"
    voice_note: voiceNote = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pushReceiverId(PushReceiverId):
    __tdlib_type__ = "pushReceiverId"
    id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class recoveryEmailAddress(RecoveryEmailAddress):
    __tdlib_type__ = "recoveryEmailAddress"
    recovery_email_address: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class remoteFile(RemoteFile):
    __tdlib_type__ = "remoteFile"
    id: str = attr.ib()
    unique_id: str = attr.ib()
    is_uploading_active: bool = attr.ib()
    is_uploading_completed: bool = attr.ib()
    uploaded_size: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class replyMarkupForceReply(ReplyMarkup):
    __tdlib_type__ = "replyMarkupForceReply"
    is_personal: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class replyMarkupInlineKeyboard(ReplyMarkup):
    __tdlib_type__ = "replyMarkupInlineKeyboard"
    rows: typing.Sequence[typing.Sequence[inlineKeyboardButton]] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class replyMarkupRemoveKeyboard(ReplyMarkup):
    __tdlib_type__ = "replyMarkupRemoveKeyboard"
    is_personal: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class replyMarkupShowKeyboard(ReplyMarkup):
    __tdlib_type__ = "replyMarkupShowKeyboard"
    rows: typing.Sequence[typing.Sequence[keyboardButton]] = attr.ib()
    resize_keyboard: bool = attr.ib()
    one_time: bool = attr.ib()
    is_personal: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTextAnchor(RichText):
    __tdlib_type__ = "richTextAnchor"
    text: RichText = attr.ib()
    name: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTextBold(RichText):
    __tdlib_type__ = "richTextBold"
    text: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTextEmailAddress(RichText):
    __tdlib_type__ = "richTextEmailAddress"
    text: RichText = attr.ib()
    email_address: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTextFixed(RichText):
    __tdlib_type__ = "richTextFixed"
    text: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTextIcon(RichText):
    __tdlib_type__ = "richTextIcon"
    document: document = attr.ib()
    width: int = attr.ib()
    height: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTextItalic(RichText):
    __tdlib_type__ = "richTextItalic"
    text: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTextMarked(RichText):
    __tdlib_type__ = "richTextMarked"
    text: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTextPhoneNumber(RichText):
    __tdlib_type__ = "richTextPhoneNumber"
    text: RichText = attr.ib()
    phone_number: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTextPlain(RichText):
    __tdlib_type__ = "richTextPlain"
    text: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTextStrikethrough(RichText):
    __tdlib_type__ = "richTextStrikethrough"
    text: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTextSubscript(RichText):
    __tdlib_type__ = "richTextSubscript"
    text: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTextSuperscript(RichText):
    __tdlib_type__ = "richTextSuperscript"
    text: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTextUnderline(RichText):
    __tdlib_type__ = "richTextUnderline"
    text: RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTextUrl(RichText):
    __tdlib_type__ = "richTextUrl"
    text: RichText = attr.ib()
    url: str = attr.ib()
    is_cached: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class richTexts(RichText):
    __tdlib_type__ = "richTexts"
    texts: typing.Sequence[RichText] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class savedCredentials(SavedCredentials):
    __tdlib_type__ = "savedCredentials"
    id: str = attr.ib()
    title: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class scopeNotificationSettings(ScopeNotificationSettings):
    __tdlib_type__ = "scopeNotificationSettings"
    mute_for: int = attr.ib()
    sound: str = attr.ib()
    show_preview: bool = attr.ib()
    disable_pinned_message_notifications: bool = attr.ib()
    disable_mention_notifications: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterAnimation(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterAnimation"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterAudio(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterAudio"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterCall(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterCall"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterChatPhoto(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterChatPhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterDocument(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterDocument"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterEmpty(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterEmpty"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterMention(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterMention"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterMissedCall(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterMissedCall"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterPhoto(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterPhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterPhotoAndVideo(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterPhotoAndVideo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterUnreadMention(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterUnreadMention"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterUrl(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterUrl"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterVideo(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterVideo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterVideoNote(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterVideoNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterVoiceAndVideoNote(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterVoiceAndVideoNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessagesFilterVoiceNote(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterVoiceNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class seconds(Seconds):
    __tdlib_type__ = "seconds"
    seconds: decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class secretChat(SecretChat):
    __tdlib_type__ = "secretChat"
    id: int = attr.ib()
    user_id: int = attr.ib()
    state: SecretChatState = attr.ib()
    is_outbound: bool = attr.ib()
    ttl: int = attr.ib()
    key_hash: bytes = attr.ib()
    layer: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class secretChatStateClosed(SecretChatState):
    __tdlib_type__ = "secretChatStateClosed"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class secretChatStatePending(SecretChatState):
    __tdlib_type__ = "secretChatStatePending"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class secretChatStateReady(SecretChatState):
    __tdlib_type__ = "secretChatStateReady"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendMessageOptions(SendMessageOptions):
    __tdlib_type__ = "sendMessageOptions"
    disable_notification: bool = attr.ib()
    from_background: bool = attr.ib()
    scheduling_state: MessageSchedulingState = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class session(Session):
    __tdlib_type__ = "session"
    id: int = attr.ib()
    is_current: bool = attr.ib()
    is_password_pending: bool = attr.ib()
    api_id: int = attr.ib()
    application_name: str = attr.ib()
    application_version: str = attr.ib()
    is_official_application: bool = attr.ib()
    device_model: str = attr.ib()
    platform: str = attr.ib()
    system_version: str = attr.ib()
    log_in_date: int = attr.ib()
    last_active_date: int = attr.ib()
    ip: str = attr.ib()
    country: str = attr.ib()
    region: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sessions(Sessions):
    __tdlib_type__ = "sessions"
    sessions: typing.Sequence[session] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class shippingOption(ShippingOption):
    __tdlib_type__ = "shippingOption"
    id: str = attr.ib()
    title: str = attr.ib()
    price_parts: typing.Sequence[labeledPricePart] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sticker(Sticker):
    __tdlib_type__ = "sticker"
    set_id: int = attr.ib()
    width: int = attr.ib()
    height: int = attr.ib()
    emoji: str = attr.ib()
    is_animated: bool = attr.ib()
    is_mask: bool = attr.ib()
    mask_position: maskPosition = attr.ib()
    thumbnail: photoSize = attr.ib()
    sticker: file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class stickerSet(StickerSet):
    __tdlib_type__ = "stickerSet"
    id: int = attr.ib()
    title: str = attr.ib()
    name: str = attr.ib()
    thumbnail: photoSize = attr.ib()
    is_installed: bool = attr.ib()
    is_archived: bool = attr.ib()
    is_official: bool = attr.ib()
    is_animated: bool = attr.ib()
    is_masks: bool = attr.ib()
    is_viewed: bool = attr.ib()
    stickers: typing.Sequence[sticker] = attr.ib()
    emojis: typing.Sequence[emojis] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class stickerSetInfo(StickerSetInfo):
    __tdlib_type__ = "stickerSetInfo"
    id: int = attr.ib()
    title: str = attr.ib()
    name: str = attr.ib()
    thumbnail: photoSize = attr.ib()
    is_installed: bool = attr.ib()
    is_archived: bool = attr.ib()
    is_official: bool = attr.ib()
    is_animated: bool = attr.ib()
    is_masks: bool = attr.ib()
    is_viewed: bool = attr.ib()
    size: int = attr.ib()
    covers: typing.Sequence[sticker] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class stickerSets(StickerSets):
    __tdlib_type__ = "stickerSets"
    total_count: int = attr.ib()
    sets: typing.Sequence[stickerSetInfo] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class stickers(Stickers):
    __tdlib_type__ = "stickers"
    stickers: typing.Sequence[sticker] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class storageStatistics(StorageStatistics):
    __tdlib_type__ = "storageStatistics"
    size: int = attr.ib()
    count: int = attr.ib()
    by_chat: typing.Sequence[storageStatisticsByChat] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class storageStatisticsByChat(StorageStatisticsByChat):
    __tdlib_type__ = "storageStatisticsByChat"
    chat_id: int = attr.ib()
    size: int = attr.ib()
    count: int = attr.ib()
    by_file_type: typing.Sequence[storageStatisticsByFileType] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class storageStatisticsByFileType(StorageStatisticsByFileType):
    __tdlib_type__ = "storageStatisticsByFileType"
    file_type: FileType = attr.ib()
    size: int = attr.ib()
    count: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class storageStatisticsFast(StorageStatisticsFast):
    __tdlib_type__ = "storageStatisticsFast"
    files_size: int = attr.ib()
    file_count: int = attr.ib()
    database_size: int = attr.ib()
    language_pack_database_size: int = attr.ib()
    log_size: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class supergroup(Supergroup):
    __tdlib_type__ = "supergroup"
    id: int = attr.ib()
    username: str = attr.ib()
    date: int = attr.ib()
    status: ChatMemberStatus = attr.ib()
    member_count: int = attr.ib()
    has_linked_chat: bool = attr.ib()
    has_location: bool = attr.ib()
    sign_messages: bool = attr.ib()
    is_slow_mode_enabled: bool = attr.ib()
    is_channel: bool = attr.ib()
    is_verified: bool = attr.ib()
    restriction_reason: str = attr.ib()
    is_scam: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class supergroupFullInfo(SupergroupFullInfo):
    __tdlib_type__ = "supergroupFullInfo"
    description: str = attr.ib()
    member_count: int = attr.ib()
    administrator_count: int = attr.ib()
    restricted_count: int = attr.ib()
    banned_count: int = attr.ib()
    linked_chat_id: int = attr.ib()
    slow_mode_delay: int = attr.ib()
    slow_mode_delay_expires_in: decimal.Decimal = attr.ib()
    can_get_members: bool = attr.ib()
    can_set_username: bool = attr.ib()
    can_set_sticker_set: bool = attr.ib()
    can_set_location: bool = attr.ib()
    can_view_statistics: bool = attr.ib()
    is_all_history_available: bool = attr.ib()
    sticker_set_id: int = attr.ib()
    location: chatLocation = attr.ib()
    invite_link: str = attr.ib()
    upgraded_from_basic_group_id: int = attr.ib()
    upgraded_from_max_message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class supergroupMembersFilterAdministrators(SupergroupMembersFilter):
    __tdlib_type__ = "supergroupMembersFilterAdministrators"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class supergroupMembersFilterBanned(SupergroupMembersFilter):
    __tdlib_type__ = "supergroupMembersFilterBanned"
    query: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class supergroupMembersFilterBots(SupergroupMembersFilter):
    __tdlib_type__ = "supergroupMembersFilterBots"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class supergroupMembersFilterContacts(SupergroupMembersFilter):
    __tdlib_type__ = "supergroupMembersFilterContacts"
    query: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class supergroupMembersFilterRecent(SupergroupMembersFilter):
    __tdlib_type__ = "supergroupMembersFilterRecent"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class supergroupMembersFilterRestricted(SupergroupMembersFilter):
    __tdlib_type__ = "supergroupMembersFilterRestricted"
    query: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class supergroupMembersFilterSearch(SupergroupMembersFilter):
    __tdlib_type__ = "supergroupMembersFilterSearch"
    query: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tMeUrl(TMeUrl):
    __tdlib_type__ = "tMeUrl"
    url: str = attr.ib()
    type: TMeUrlType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tMeUrlTypeChatInvite(TMeUrlType):
    __tdlib_type__ = "tMeUrlTypeChatInvite"
    info: chatInviteLinkInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tMeUrlTypeStickerSet(TMeUrlType):
    __tdlib_type__ = "tMeUrlTypeStickerSet"
    sticker_set_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tMeUrlTypeSupergroup(TMeUrlType):
    __tdlib_type__ = "tMeUrlTypeSupergroup"
    supergroup_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tMeUrlTypeUser(TMeUrlType):
    __tdlib_type__ = "tMeUrlTypeUser"
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tMeUrls(TMeUrls):
    __tdlib_type__ = "tMeUrls"
    urls: typing.Sequence[tMeUrl] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlibParameters(TdlibParameters):
    __tdlib_type__ = "tdlibParameters"
    use_test_dc: bool = attr.ib()
    database_directory: str = attr.ib()
    files_directory: str = attr.ib()
    use_file_database: bool = attr.ib()
    use_chat_info_database: bool = attr.ib()
    use_message_database: bool = attr.ib()
    use_secret_chats: bool = attr.ib()
    api_id: int = attr.ib()
    api_hash: str = attr.ib()
    system_language_code: str = attr.ib()
    device_model: str = attr.ib()
    system_version: str = attr.ib()
    application_version: str = attr.ib()
    enable_storage_optimizer: bool = attr.ib()
    ignore_file_names: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class temporaryPasswordState(TemporaryPasswordState):
    __tdlib_type__ = "temporaryPasswordState"
    has_password: bool = attr.ib()
    valid_for: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class termsOfService(TermsOfService):
    __tdlib_type__ = "termsOfService"
    text: formattedText = attr.ib()
    min_user_age: int = attr.ib()
    show_popup: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testBytes(TestBytes):
    __tdlib_type__ = "testBytes"
    value: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testInt(TestInt):
    __tdlib_type__ = "testInt"
    value: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testString(TestString):
    __tdlib_type__ = "testString"
    value: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testVectorInt(TestVectorInt):
    __tdlib_type__ = "testVectorInt"
    value: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testVectorIntObject(TestVectorIntObject):
    __tdlib_type__ = "testVectorIntObject"
    value: typing.Sequence[testInt] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testVectorString(TestVectorString):
    __tdlib_type__ = "testVectorString"
    value: typing.Sequence[str] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testVectorStringObject(TestVectorStringObject):
    __tdlib_type__ = "testVectorStringObject"
    value: typing.Sequence[testString] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class text(Text):
    __tdlib_type__ = "text"
    text: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntities(TextEntities):
    __tdlib_type__ = "textEntities"
    entities: typing.Sequence[textEntity] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntity(TextEntity):
    __tdlib_type__ = "textEntity"
    offset: int = attr.ib()
    length: int = attr.ib()
    type: TextEntityType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypeBold(TextEntityType):
    __tdlib_type__ = "textEntityTypeBold"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypeBotCommand(TextEntityType):
    __tdlib_type__ = "textEntityTypeBotCommand"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypeCashtag(TextEntityType):
    __tdlib_type__ = "textEntityTypeCashtag"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypeCode(TextEntityType):
    __tdlib_type__ = "textEntityTypeCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypeEmailAddress(TextEntityType):
    __tdlib_type__ = "textEntityTypeEmailAddress"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypeHashtag(TextEntityType):
    __tdlib_type__ = "textEntityTypeHashtag"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypeItalic(TextEntityType):
    __tdlib_type__ = "textEntityTypeItalic"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypeMention(TextEntityType):
    __tdlib_type__ = "textEntityTypeMention"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypeMentionName(TextEntityType):
    __tdlib_type__ = "textEntityTypeMentionName"
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypePhoneNumber(TextEntityType):
    __tdlib_type__ = "textEntityTypePhoneNumber"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypePre(TextEntityType):
    __tdlib_type__ = "textEntityTypePre"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypePreCode(TextEntityType):
    __tdlib_type__ = "textEntityTypePreCode"
    language: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypeStrikethrough(TextEntityType):
    __tdlib_type__ = "textEntityTypeStrikethrough"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypeTextUrl(TextEntityType):
    __tdlib_type__ = "textEntityTypeTextUrl"
    url: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypeUnderline(TextEntityType):
    __tdlib_type__ = "textEntityTypeUnderline"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textEntityTypeUrl(TextEntityType):
    __tdlib_type__ = "textEntityTypeUrl"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textParseModeHTML(TextParseMode):
    __tdlib_type__ = "textParseModeHTML"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class textParseModeMarkdown(TextParseMode):
    __tdlib_type__ = "textParseModeMarkdown"
    version: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tonLiteServerResponse(TonLiteServerResponse):
    __tdlib_type__ = "tonLiteServerResponse"
    response: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tonWalletPasswordSalt(TonWalletPasswordSalt):
    __tdlib_type__ = "tonWalletPasswordSalt"
    salt: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class topChatCategoryBots(TopChatCategory):
    __tdlib_type__ = "topChatCategoryBots"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class topChatCategoryCalls(TopChatCategory):
    __tdlib_type__ = "topChatCategoryCalls"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class topChatCategoryChannels(TopChatCategory):
    __tdlib_type__ = "topChatCategoryChannels"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class topChatCategoryForwardChats(TopChatCategory):
    __tdlib_type__ = "topChatCategoryForwardChats"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class topChatCategoryGroups(TopChatCategory):
    __tdlib_type__ = "topChatCategoryGroups"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class topChatCategoryInlineBots(TopChatCategory):
    __tdlib_type__ = "topChatCategoryInlineBots"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class topChatCategoryUsers(TopChatCategory):
    __tdlib_type__ = "topChatCategoryUsers"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateActiveNotifications(Update):
    __tdlib_type__ = "updateActiveNotifications"
    groups: typing.Sequence[notificationGroup] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateAuthorizationState(Update):
    __tdlib_type__ = "updateAuthorizationState"
    authorization_state: AuthorizationState = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateBasicGroup(Update):
    __tdlib_type__ = "updateBasicGroup"
    basic_group: basicGroup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateBasicGroupFullInfo(Update):
    __tdlib_type__ = "updateBasicGroupFullInfo"
    basic_group_id: int = attr.ib()
    basic_group_full_info: basicGroupFullInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateCall(Update):
    __tdlib_type__ = "updateCall"
    call: call = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatActionBar(Update):
    __tdlib_type__ = "updateChatActionBar"
    chat_id: int = attr.ib()
    action_bar: ChatActionBar = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatChatList(Update):
    __tdlib_type__ = "updateChatChatList"
    chat_id: int = attr.ib()
    chat_list: ChatList = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatDefaultDisableNotification(Update):
    __tdlib_type__ = "updateChatDefaultDisableNotification"
    chat_id: int = attr.ib()
    default_disable_notification: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatDraftMessage(Update):
    __tdlib_type__ = "updateChatDraftMessage"
    chat_id: int = attr.ib()
    draft_message: draftMessage = attr.ib()
    order: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatHasScheduledMessages(Update):
    __tdlib_type__ = "updateChatHasScheduledMessages"
    chat_id: int = attr.ib()
    has_scheduled_messages: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatIsMarkedAsUnread(Update):
    __tdlib_type__ = "updateChatIsMarkedAsUnread"
    chat_id: int = attr.ib()
    is_marked_as_unread: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatIsPinned(Update):
    __tdlib_type__ = "updateChatIsPinned"
    chat_id: int = attr.ib()
    is_pinned: bool = attr.ib()
    order: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatIsSponsored(Update):
    __tdlib_type__ = "updateChatIsSponsored"
    chat_id: int = attr.ib()
    is_sponsored: bool = attr.ib()
    order: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatLastMessage(Update):
    __tdlib_type__ = "updateChatLastMessage"
    chat_id: int = attr.ib()
    last_message: message = attr.ib()
    order: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatNotificationSettings(Update):
    __tdlib_type__ = "updateChatNotificationSettings"
    chat_id: int = attr.ib()
    notification_settings: chatNotificationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatOnlineMemberCount(Update):
    __tdlib_type__ = "updateChatOnlineMemberCount"
    chat_id: int = attr.ib()
    online_member_count: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatOrder(Update):
    __tdlib_type__ = "updateChatOrder"
    chat_id: int = attr.ib()
    order: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatPermissions(Update):
    __tdlib_type__ = "updateChatPermissions"
    chat_id: int = attr.ib()
    permissions: chatPermissions = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatPhoto(Update):
    __tdlib_type__ = "updateChatPhoto"
    chat_id: int = attr.ib()
    photo: chatPhoto = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatPinnedMessage(Update):
    __tdlib_type__ = "updateChatPinnedMessage"
    chat_id: int = attr.ib()
    pinned_message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatReadInbox(Update):
    __tdlib_type__ = "updateChatReadInbox"
    chat_id: int = attr.ib()
    last_read_inbox_message_id: int = attr.ib()
    unread_count: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatReadOutbox(Update):
    __tdlib_type__ = "updateChatReadOutbox"
    chat_id: int = attr.ib()
    last_read_outbox_message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatReplyMarkup(Update):
    __tdlib_type__ = "updateChatReplyMarkup"
    chat_id: int = attr.ib()
    reply_markup_message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatTitle(Update):
    __tdlib_type__ = "updateChatTitle"
    chat_id: int = attr.ib()
    title: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateChatUnreadMentionCount(Update):
    __tdlib_type__ = "updateChatUnreadMentionCount"
    chat_id: int = attr.ib()
    unread_mention_count: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateConnectionState(Update):
    __tdlib_type__ = "updateConnectionState"
    state: ConnectionState = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateDeleteMessages(Update):
    __tdlib_type__ = "updateDeleteMessages"
    chat_id: int = attr.ib()
    message_ids: typing.Sequence[int] = attr.ib()
    is_permanent: bool = attr.ib()
    from_cache: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateFavoriteStickers(Update):
    __tdlib_type__ = "updateFavoriteStickers"
    sticker_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateFile(Update):
    __tdlib_type__ = "updateFile"
    file: file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateFileGenerationStart(Update):
    __tdlib_type__ = "updateFileGenerationStart"
    generation_id: int = attr.ib()
    original_path: str = attr.ib()
    destination_path: str = attr.ib()
    conversion: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateFileGenerationStop(Update):
    __tdlib_type__ = "updateFileGenerationStop"
    generation_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateHavePendingNotifications(Update):
    __tdlib_type__ = "updateHavePendingNotifications"
    have_delayed_notifications: bool = attr.ib()
    have_unreceived_notifications: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateInstalledStickerSets(Update):
    __tdlib_type__ = "updateInstalledStickerSets"
    is_masks: bool = attr.ib()
    sticker_set_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateLanguagePackStrings(Update):
    __tdlib_type__ = "updateLanguagePackStrings"
    localization_target: str = attr.ib()
    language_pack_id: str = attr.ib()
    strings: typing.Sequence[languagePackString] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateMessageContent(Update):
    __tdlib_type__ = "updateMessageContent"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    new_content: MessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateMessageContentOpened(Update):
    __tdlib_type__ = "updateMessageContentOpened"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateMessageEdited(Update):
    __tdlib_type__ = "updateMessageEdited"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    edit_date: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateMessageLiveLocationViewed(Update):
    __tdlib_type__ = "updateMessageLiveLocationViewed"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateMessageMentionRead(Update):
    __tdlib_type__ = "updateMessageMentionRead"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    unread_mention_count: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateMessageSendAcknowledged(Update):
    __tdlib_type__ = "updateMessageSendAcknowledged"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateMessageSendFailed(Update):
    __tdlib_type__ = "updateMessageSendFailed"
    message: message = attr.ib()
    old_message_id: int = attr.ib()
    error_code: int = attr.ib()
    error_message: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateMessageSendSucceeded(Update):
    __tdlib_type__ = "updateMessageSendSucceeded"
    message: message = attr.ib()
    old_message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateMessageViews(Update):
    __tdlib_type__ = "updateMessageViews"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    views: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateNewCallbackQuery(Update):
    __tdlib_type__ = "updateNewCallbackQuery"
    id: int = attr.ib()
    sender_user_id: int = attr.ib()
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    chat_instance: int = attr.ib()
    payload: CallbackQueryPayload = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateNewChat(Update):
    __tdlib_type__ = "updateNewChat"
    chat: chat = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateNewChosenInlineResult(Update):
    __tdlib_type__ = "updateNewChosenInlineResult"
    sender_user_id: int = attr.ib()
    user_location: location = attr.ib()
    query: str = attr.ib()
    result_id: str = attr.ib()
    inline_message_id: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateNewCustomEvent(Update):
    __tdlib_type__ = "updateNewCustomEvent"
    event: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateNewCustomQuery(Update):
    __tdlib_type__ = "updateNewCustomQuery"
    id: int = attr.ib()
    data: str = attr.ib()
    timeout: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateNewInlineCallbackQuery(Update):
    __tdlib_type__ = "updateNewInlineCallbackQuery"
    id: int = attr.ib()
    sender_user_id: int = attr.ib()
    inline_message_id: str = attr.ib()
    chat_instance: int = attr.ib()
    payload: CallbackQueryPayload = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateNewInlineQuery(Update):
    __tdlib_type__ = "updateNewInlineQuery"
    id: int = attr.ib()
    sender_user_id: int = attr.ib()
    user_location: location = attr.ib()
    query: str = attr.ib()
    offset: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateNewMessage(Update):
    __tdlib_type__ = "updateNewMessage"
    message: message = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateNewPreCheckoutQuery(Update):
    __tdlib_type__ = "updateNewPreCheckoutQuery"
    id: int = attr.ib()
    sender_user_id: int = attr.ib()
    currency: str = attr.ib()
    total_amount: int = attr.ib()
    invoice_payload: bytes = attr.ib()
    shipping_option_id: str = attr.ib()
    order_info: orderInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateNewShippingQuery(Update):
    __tdlib_type__ = "updateNewShippingQuery"
    id: int = attr.ib()
    sender_user_id: int = attr.ib()
    invoice_payload: str = attr.ib()
    shipping_address: address = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateNotification(Update):
    __tdlib_type__ = "updateNotification"
    notification_group_id: int = attr.ib()
    notification: notification = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateNotificationGroup(Update):
    __tdlib_type__ = "updateNotificationGroup"
    notification_group_id: int = attr.ib()
    type: NotificationGroupType = attr.ib()
    chat_id: int = attr.ib()
    notification_settings_chat_id: int = attr.ib()
    is_silent: bool = attr.ib()
    total_count: int = attr.ib()
    added_notifications: typing.Sequence[notification] = attr.ib()
    removed_notification_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateOption(Update):
    __tdlib_type__ = "updateOption"
    name: str = attr.ib()
    value: OptionValue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updatePoll(Update):
    __tdlib_type__ = "updatePoll"
    poll: poll = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateRecentStickers(Update):
    __tdlib_type__ = "updateRecentStickers"
    is_attached: bool = attr.ib()
    sticker_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateSavedAnimations(Update):
    __tdlib_type__ = "updateSavedAnimations"
    animation_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateScopeNotificationSettings(Update):
    __tdlib_type__ = "updateScopeNotificationSettings"
    scope: NotificationSettingsScope = attr.ib()
    notification_settings: scopeNotificationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateSecretChat(Update):
    __tdlib_type__ = "updateSecretChat"
    secret_chat: secretChat = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateSelectedBackground(Update):
    __tdlib_type__ = "updateSelectedBackground"
    for_dark_theme: bool = attr.ib()
    background: background = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateServiceNotification(Update):
    __tdlib_type__ = "updateServiceNotification"
    type: str = attr.ib()
    content: MessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateSupergroup(Update):
    __tdlib_type__ = "updateSupergroup"
    supergroup: supergroup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateSupergroupFullInfo(Update):
    __tdlib_type__ = "updateSupergroupFullInfo"
    supergroup_id: int = attr.ib()
    supergroup_full_info: supergroupFullInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateTermsOfService(Update):
    __tdlib_type__ = "updateTermsOfService"
    terms_of_service_id: str = attr.ib()
    terms_of_service: termsOfService = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateTrendingStickerSets(Update):
    __tdlib_type__ = "updateTrendingStickerSets"
    sticker_sets: stickerSets = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateUnreadChatCount(Update):
    __tdlib_type__ = "updateUnreadChatCount"
    chat_list: ChatList = attr.ib()
    total_count: int = attr.ib()
    unread_count: int = attr.ib()
    unread_unmuted_count: int = attr.ib()
    marked_as_unread_count: int = attr.ib()
    marked_as_unread_unmuted_count: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateUnreadMessageCount(Update):
    __tdlib_type__ = "updateUnreadMessageCount"
    chat_list: ChatList = attr.ib()
    unread_count: int = attr.ib()
    unread_unmuted_count: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateUser(Update):
    __tdlib_type__ = "updateUser"
    user: user = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateUserChatAction(Update):
    __tdlib_type__ = "updateUserChatAction"
    chat_id: int = attr.ib()
    user_id: int = attr.ib()
    action: ChatAction = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateUserFullInfo(Update):
    __tdlib_type__ = "updateUserFullInfo"
    user_id: int = attr.ib()
    user_full_info: userFullInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateUserPrivacySettingRules(Update):
    __tdlib_type__ = "updateUserPrivacySettingRules"
    setting: UserPrivacySetting = attr.ib()
    rules: userPrivacySettingRules = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateUserStatus(Update):
    __tdlib_type__ = "updateUserStatus"
    user_id: int = attr.ib()
    status: UserStatus = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updateUsersNearby(Update):
    __tdlib_type__ = "updateUsersNearby"
    users_nearby: typing.Sequence[chatNearby] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class updates(Updates):
    __tdlib_type__ = "updates"
    updates: typing.Sequence[Update] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class user(User):
    __tdlib_type__ = "user"
    id: int = attr.ib()
    first_name: str = attr.ib()
    last_name: str = attr.ib()
    username: str = attr.ib()
    phone_number: str = attr.ib()
    status: UserStatus = attr.ib()
    profile_photo: profilePhoto = attr.ib()
    is_contact: bool = attr.ib()
    is_mutual_contact: bool = attr.ib()
    is_verified: bool = attr.ib()
    is_support: bool = attr.ib()
    restriction_reason: str = attr.ib()
    is_scam: bool = attr.ib()
    have_access: bool = attr.ib()
    type: UserType = attr.ib()
    language_code: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userFullInfo(UserFullInfo):
    __tdlib_type__ = "userFullInfo"
    is_blocked: bool = attr.ib()
    can_be_called: bool = attr.ib()
    has_private_calls: bool = attr.ib()
    need_phone_number_privacy_exception: bool = attr.ib()
    bio: str = attr.ib()
    share_text: str = attr.ib()
    group_in_common_count: int = attr.ib()
    bot_info: botInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingAllowCalls(UserPrivacySetting):
    __tdlib_type__ = "userPrivacySettingAllowCalls"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingAllowChatInvites(UserPrivacySetting):
    __tdlib_type__ = "userPrivacySettingAllowChatInvites"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingAllowFindingByPhoneNumber(UserPrivacySetting):
    __tdlib_type__ = "userPrivacySettingAllowFindingByPhoneNumber"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingAllowPeerToPeerCalls(UserPrivacySetting):
    __tdlib_type__ = "userPrivacySettingAllowPeerToPeerCalls"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingRuleAllowAll(UserPrivacySettingRule):
    __tdlib_type__ = "userPrivacySettingRuleAllowAll"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingRuleAllowChatMembers(UserPrivacySettingRule):
    __tdlib_type__ = "userPrivacySettingRuleAllowChatMembers"
    chat_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingRuleAllowContacts(UserPrivacySettingRule):
    __tdlib_type__ = "userPrivacySettingRuleAllowContacts"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingRuleAllowUsers(UserPrivacySettingRule):
    __tdlib_type__ = "userPrivacySettingRuleAllowUsers"
    user_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingRuleRestrictAll(UserPrivacySettingRule):
    __tdlib_type__ = "userPrivacySettingRuleRestrictAll"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingRuleRestrictChatMembers(UserPrivacySettingRule):
    __tdlib_type__ = "userPrivacySettingRuleRestrictChatMembers"
    chat_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingRuleRestrictContacts(UserPrivacySettingRule):
    __tdlib_type__ = "userPrivacySettingRuleRestrictContacts"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingRuleRestrictUsers(UserPrivacySettingRule):
    __tdlib_type__ = "userPrivacySettingRuleRestrictUsers"
    user_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingRules(UserPrivacySettingRules):
    __tdlib_type__ = "userPrivacySettingRules"
    rules: typing.Sequence[UserPrivacySettingRule] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingShowLinkInForwardedMessages(UserPrivacySetting):
    __tdlib_type__ = "userPrivacySettingShowLinkInForwardedMessages"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingShowPhoneNumber(UserPrivacySetting):
    __tdlib_type__ = "userPrivacySettingShowPhoneNumber"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingShowProfilePhoto(UserPrivacySetting):
    __tdlib_type__ = "userPrivacySettingShowProfilePhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userPrivacySettingShowStatus(UserPrivacySetting):
    __tdlib_type__ = "userPrivacySettingShowStatus"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userProfilePhoto(UserProfilePhoto):
    __tdlib_type__ = "userProfilePhoto"
    id: int = attr.ib()
    added_date: int = attr.ib()
    sizes: typing.Sequence[photoSize] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userProfilePhotos(UserProfilePhotos):
    __tdlib_type__ = "userProfilePhotos"
    total_count: int = attr.ib()
    photos: typing.Sequence[userProfilePhoto] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userStatusEmpty(UserStatus):
    __tdlib_type__ = "userStatusEmpty"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userStatusLastMonth(UserStatus):
    __tdlib_type__ = "userStatusLastMonth"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userStatusLastWeek(UserStatus):
    __tdlib_type__ = "userStatusLastWeek"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userStatusOffline(UserStatus):
    __tdlib_type__ = "userStatusOffline"
    was_online: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userStatusOnline(UserStatus):
    __tdlib_type__ = "userStatusOnline"
    expires: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userStatusRecently(UserStatus):
    __tdlib_type__ = "userStatusRecently"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userTypeBot(UserType):
    __tdlib_type__ = "userTypeBot"
    can_join_groups: bool = attr.ib()
    can_read_all_group_messages: bool = attr.ib()
    is_inline: bool = attr.ib()
    inline_query_placeholder: str = attr.ib()
    need_location: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userTypeDeleted(UserType):
    __tdlib_type__ = "userTypeDeleted"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userTypeRegular(UserType):
    __tdlib_type__ = "userTypeRegular"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class userTypeUnknown(UserType):
    __tdlib_type__ = "userTypeUnknown"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class users(Users):
    __tdlib_type__ = "users"
    total_count: int = attr.ib()
    user_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class validatedOrderInfo(ValidatedOrderInfo):
    __tdlib_type__ = "validatedOrderInfo"
    order_info_id: str = attr.ib()
    shipping_options: typing.Sequence[shippingOption] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class venue(Venue):
    __tdlib_type__ = "venue"
    location: location = attr.ib()
    title: str = attr.ib()
    address: str = attr.ib()
    provider: str = attr.ib()
    id: str = attr.ib()
    type: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class video(Video):
    __tdlib_type__ = "video"
    duration: int = attr.ib()
    width: int = attr.ib()
    height: int = attr.ib()
    file_name: str = attr.ib()
    mime_type: str = attr.ib()
    has_stickers: bool = attr.ib()
    supports_streaming: bool = attr.ib()
    minithumbnail: minithumbnail = attr.ib()
    thumbnail: photoSize = attr.ib()
    video: file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class videoNote(VideoNote):
    __tdlib_type__ = "videoNote"
    duration: int = attr.ib()
    length: int = attr.ib()
    minithumbnail: minithumbnail = attr.ib()
    thumbnail: photoSize = attr.ib()
    video: file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class voiceNote(VoiceNote):
    __tdlib_type__ = "voiceNote"
    duration: int = attr.ib()
    waveform: bytes = attr.ib()
    mime_type: str = attr.ib()
    voice: file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class webPage(WebPage):
    __tdlib_type__ = "webPage"
    url: str = attr.ib()
    display_url: str = attr.ib()
    type: str = attr.ib()
    site_name: str = attr.ib()
    title: str = attr.ib()
    description: str = attr.ib()
    photo: photo = attr.ib()
    embed_url: str = attr.ib()
    embed_type: str = attr.ib()
    embed_width: int = attr.ib()
    embed_height: int = attr.ib()
    duration: int = attr.ib()
    author: str = attr.ib()
    animation: animation = attr.ib()
    audio: audio = attr.ib()
    document: document = attr.ib()
    sticker: sticker = attr.ib()
    video: video = attr.ib()
    video_note: videoNote = attr.ib()
    voice_note: voiceNote = attr.ib()
    instant_view_version: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class webPageInstantView(WebPageInstantView):
    __tdlib_type__ = "webPageInstantView"
    page_blocks: typing.Sequence[PageBlock] = attr.ib()
    version: int = attr.ib()
    url: str = attr.ib()
    is_rtl: bool = attr.ib()
    is_full: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getAuthorizationState(RootObject):
    __tdlib_type__ = "getAuthorizationState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setTdlibParameters(RootObject):
    __tdlib_type__ = "setTdlibParameters"
    parameters: tdlibParameters = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkDatabaseEncryptionKey(RootObject):
    __tdlib_type__ = "checkDatabaseEncryptionKey"
    key: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setAuthenticationPhoneNumber(RootObject):
    __tdlib_type__ = "setAuthenticationPhoneNumber"
    phone_number: str = attr.ib()
    settings: phoneNumberAuthenticationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class resendAuthenticationCode(RootObject):
    __tdlib_type__ = "resendAuthenticationCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkAuthenticationCode(RootObject):
    __tdlib_type__ = "checkAuthenticationCode"
    code: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class requestQrCodeAuthentication(RootObject):
    __tdlib_type__ = "requestQrCodeAuthentication"
    other_user_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class registerUser(RootObject):
    __tdlib_type__ = "registerUser"
    first_name: str = attr.ib()
    last_name: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkAuthenticationPassword(RootObject):
    __tdlib_type__ = "checkAuthenticationPassword"
    password: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class requestAuthenticationPasswordRecovery(RootObject):
    __tdlib_type__ = "requestAuthenticationPasswordRecovery"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class recoverAuthenticationPassword(RootObject):
    __tdlib_type__ = "recoverAuthenticationPassword"
    recovery_code: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkAuthenticationBotToken(RootObject):
    __tdlib_type__ = "checkAuthenticationBotToken"
    token: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class logOut(RootObject):
    __tdlib_type__ = "logOut"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class close(RootObject):
    __tdlib_type__ = "close"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class destroy(RootObject):
    __tdlib_type__ = "destroy"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class confirmQrCodeAuthentication(RootObject):
    __tdlib_type__ = "confirmQrCodeAuthentication"
    link: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getCurrentState(RootObject):
    __tdlib_type__ = "getCurrentState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setDatabaseEncryptionKey(RootObject):
    __tdlib_type__ = "setDatabaseEncryptionKey"
    new_encryption_key: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getPasswordState(RootObject):
    __tdlib_type__ = "getPasswordState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setPassword(RootObject):
    __tdlib_type__ = "setPassword"
    old_password: str = attr.ib()
    new_password: str = attr.ib()
    new_hint: str = attr.ib()
    set_recovery_email_address: bool = attr.ib()
    new_recovery_email_address: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getRecoveryEmailAddress(RootObject):
    __tdlib_type__ = "getRecoveryEmailAddress"
    password: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setRecoveryEmailAddress(RootObject):
    __tdlib_type__ = "setRecoveryEmailAddress"
    password: str = attr.ib()
    new_recovery_email_address: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkRecoveryEmailAddressCode(RootObject):
    __tdlib_type__ = "checkRecoveryEmailAddressCode"
    code: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class resendRecoveryEmailAddressCode(RootObject):
    __tdlib_type__ = "resendRecoveryEmailAddressCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class requestPasswordRecovery(RootObject):
    __tdlib_type__ = "requestPasswordRecovery"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class recoverPassword(RootObject):
    __tdlib_type__ = "recoverPassword"
    recovery_code: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class createTemporaryPassword(RootObject):
    __tdlib_type__ = "createTemporaryPassword"
    password: str = attr.ib()
    valid_for: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getTemporaryPasswordState(RootObject):
    __tdlib_type__ = "getTemporaryPasswordState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getMe(RootObject):
    __tdlib_type__ = "getMe"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getUser(RootObject):
    __tdlib_type__ = "getUser"
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getUserFullInfo(RootObject):
    __tdlib_type__ = "getUserFullInfo"
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getBasicGroup(RootObject):
    __tdlib_type__ = "getBasicGroup"
    basic_group_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getBasicGroupFullInfo(RootObject):
    __tdlib_type__ = "getBasicGroupFullInfo"
    basic_group_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getSupergroup(RootObject):
    __tdlib_type__ = "getSupergroup"
    supergroup_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getSupergroupFullInfo(RootObject):
    __tdlib_type__ = "getSupergroupFullInfo"
    supergroup_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getSecretChat(RootObject):
    __tdlib_type__ = "getSecretChat"
    secret_chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getChat(RootObject):
    __tdlib_type__ = "getChat"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getMessage(RootObject):
    __tdlib_type__ = "getMessage"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getMessageLocally(RootObject):
    __tdlib_type__ = "getMessageLocally"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getRepliedMessage(RootObject):
    __tdlib_type__ = "getRepliedMessage"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getChatPinnedMessage(RootObject):
    __tdlib_type__ = "getChatPinnedMessage"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getMessages(RootObject):
    __tdlib_type__ = "getMessages"
    chat_id: int = attr.ib()
    message_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getFile(RootObject):
    __tdlib_type__ = "getFile"
    file_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getRemoteFile(RootObject):
    __tdlib_type__ = "getRemoteFile"
    remote_file_id: str = attr.ib()
    file_type: FileType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getChats(RootObject):
    __tdlib_type__ = "getChats"
    chat_list: ChatList = attr.ib()
    offset_order: int = attr.ib()
    offset_chat_id: int = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchPublicChat(RootObject):
    __tdlib_type__ = "searchPublicChat"
    username: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchPublicChats(RootObject):
    __tdlib_type__ = "searchPublicChats"
    query: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchChats(RootObject):
    __tdlib_type__ = "searchChats"
    query: str = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchChatsOnServer(RootObject):
    __tdlib_type__ = "searchChatsOnServer"
    query: str = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchChatsNearby(RootObject):
    __tdlib_type__ = "searchChatsNearby"
    location: location = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getTopChats(RootObject):
    __tdlib_type__ = "getTopChats"
    category: TopChatCategory = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class removeTopChat(RootObject):
    __tdlib_type__ = "removeTopChat"
    category: TopChatCategory = attr.ib()
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class addRecentlyFoundChat(RootObject):
    __tdlib_type__ = "addRecentlyFoundChat"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class removeRecentlyFoundChat(RootObject):
    __tdlib_type__ = "removeRecentlyFoundChat"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class clearRecentlyFoundChats(RootObject):
    __tdlib_type__ = "clearRecentlyFoundChats"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkChatUsername(RootObject):
    __tdlib_type__ = "checkChatUsername"
    chat_id: int = attr.ib()
    username: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getCreatedPublicChats(RootObject):
    __tdlib_type__ = "getCreatedPublicChats"
    type: PublicChatType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkCreatedPublicChatsLimit(RootObject):
    __tdlib_type__ = "checkCreatedPublicChatsLimit"
    type: PublicChatType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getSuitableDiscussionChats(RootObject):
    __tdlib_type__ = "getSuitableDiscussionChats"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getInactiveSupergroupChats(RootObject):
    __tdlib_type__ = "getInactiveSupergroupChats"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getGroupsInCommon(RootObject):
    __tdlib_type__ = "getGroupsInCommon"
    user_id: int = attr.ib()
    offset_chat_id: int = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getChatHistory(RootObject):
    __tdlib_type__ = "getChatHistory"
    chat_id: int = attr.ib()
    from_message_id: int = attr.ib()
    offset: int = attr.ib()
    limit: int = attr.ib()
    only_local: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deleteChatHistory(RootObject):
    __tdlib_type__ = "deleteChatHistory"
    chat_id: int = attr.ib()
    remove_from_chat_list: bool = attr.ib()
    revoke: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchChatMessages(RootObject):
    __tdlib_type__ = "searchChatMessages"
    chat_id: int = attr.ib()
    query: str = attr.ib()
    sender_user_id: int = attr.ib()
    from_message_id: int = attr.ib()
    offset: int = attr.ib()
    limit: int = attr.ib()
    filter: SearchMessagesFilter = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchMessages(RootObject):
    __tdlib_type__ = "searchMessages"
    chat_list: ChatList = attr.ib()
    query: str = attr.ib()
    offset_date: int = attr.ib()
    offset_chat_id: int = attr.ib()
    offset_message_id: int = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchSecretMessages(RootObject):
    __tdlib_type__ = "searchSecretMessages"
    chat_id: int = attr.ib()
    query: str = attr.ib()
    from_search_id: int = attr.ib()
    limit: int = attr.ib()
    filter: SearchMessagesFilter = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchCallMessages(RootObject):
    __tdlib_type__ = "searchCallMessages"
    from_message_id: int = attr.ib()
    limit: int = attr.ib()
    only_missed: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchChatRecentLocationMessages(RootObject):
    __tdlib_type__ = "searchChatRecentLocationMessages"
    chat_id: int = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getActiveLiveLocationMessages(RootObject):
    __tdlib_type__ = "getActiveLiveLocationMessages"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getChatMessageByDate(RootObject):
    __tdlib_type__ = "getChatMessageByDate"
    chat_id: int = attr.ib()
    date: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getChatMessageCount(RootObject):
    __tdlib_type__ = "getChatMessageCount"
    chat_id: int = attr.ib()
    filter: SearchMessagesFilter = attr.ib()
    return_local: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getChatScheduledMessages(RootObject):
    __tdlib_type__ = "getChatScheduledMessages"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class removeNotification(RootObject):
    __tdlib_type__ = "removeNotification"
    notification_group_id: int = attr.ib()
    notification_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class removeNotificationGroup(RootObject):
    __tdlib_type__ = "removeNotificationGroup"
    notification_group_id: int = attr.ib()
    max_notification_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getPublicMessageLink(RootObject):
    __tdlib_type__ = "getPublicMessageLink"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    for_album: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getMessageLink(RootObject):
    __tdlib_type__ = "getMessageLink"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getMessageLinkInfo(RootObject):
    __tdlib_type__ = "getMessageLinkInfo"
    url: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendMessage(RootObject):
    __tdlib_type__ = "sendMessage"
    chat_id: int = attr.ib()
    reply_to_message_id: int = attr.ib()
    options: sendMessageOptions = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendMessageAlbum(RootObject):
    __tdlib_type__ = "sendMessageAlbum"
    chat_id: int = attr.ib()
    reply_to_message_id: int = attr.ib()
    options: sendMessageOptions = attr.ib()
    input_message_contents: typing.Sequence[InputMessageContent] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendBotStartMessage(RootObject):
    __tdlib_type__ = "sendBotStartMessage"
    bot_user_id: int = attr.ib()
    chat_id: int = attr.ib()
    parameter: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendInlineQueryResultMessage(RootObject):
    __tdlib_type__ = "sendInlineQueryResultMessage"
    chat_id: int = attr.ib()
    reply_to_message_id: int = attr.ib()
    options: sendMessageOptions = attr.ib()
    query_id: int = attr.ib()
    result_id: str = attr.ib()
    hide_via_bot: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class forwardMessages(RootObject):
    __tdlib_type__ = "forwardMessages"
    chat_id: int = attr.ib()
    from_chat_id: int = attr.ib()
    message_ids: typing.Sequence[int] = attr.ib()
    options: sendMessageOptions = attr.ib()
    as_album: bool = attr.ib()
    send_copy: bool = attr.ib()
    remove_caption: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class resendMessages(RootObject):
    __tdlib_type__ = "resendMessages"
    chat_id: int = attr.ib()
    message_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendChatSetTtlMessage(RootObject):
    __tdlib_type__ = "sendChatSetTtlMessage"
    chat_id: int = attr.ib()
    ttl: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendChatScreenshotTakenNotification(RootObject):
    __tdlib_type__ = "sendChatScreenshotTakenNotification"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class addLocalMessage(RootObject):
    __tdlib_type__ = "addLocalMessage"
    chat_id: int = attr.ib()
    sender_user_id: int = attr.ib()
    reply_to_message_id: int = attr.ib()
    disable_notification: bool = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deleteMessages(RootObject):
    __tdlib_type__ = "deleteMessages"
    chat_id: int = attr.ib()
    message_ids: typing.Sequence[int] = attr.ib()
    revoke: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deleteChatMessagesFromUser(RootObject):
    __tdlib_type__ = "deleteChatMessagesFromUser"
    chat_id: int = attr.ib()
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class editMessageText(RootObject):
    __tdlib_type__ = "editMessageText"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class editMessageLiveLocation(RootObject):
    __tdlib_type__ = "editMessageLiveLocation"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    location: location = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class editMessageMedia(RootObject):
    __tdlib_type__ = "editMessageMedia"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class editMessageCaption(RootObject):
    __tdlib_type__ = "editMessageCaption"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    caption: formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class editMessageReplyMarkup(RootObject):
    __tdlib_type__ = "editMessageReplyMarkup"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class editInlineMessageText(RootObject):
    __tdlib_type__ = "editInlineMessageText"
    inline_message_id: str = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class editInlineMessageLiveLocation(RootObject):
    __tdlib_type__ = "editInlineMessageLiveLocation"
    inline_message_id: str = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    location: location = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class editInlineMessageMedia(RootObject):
    __tdlib_type__ = "editInlineMessageMedia"
    inline_message_id: str = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    input_message_content: InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class editInlineMessageCaption(RootObject):
    __tdlib_type__ = "editInlineMessageCaption"
    inline_message_id: str = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()
    caption: formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class editInlineMessageReplyMarkup(RootObject):
    __tdlib_type__ = "editInlineMessageReplyMarkup"
    inline_message_id: str = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class editMessageSchedulingState(RootObject):
    __tdlib_type__ = "editMessageSchedulingState"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    scheduling_state: MessageSchedulingState = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getTextEntities(RootObject):
    __tdlib_type__ = "getTextEntities"
    text: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class parseTextEntities(RootObject):
    __tdlib_type__ = "parseTextEntities"
    text: str = attr.ib()
    parse_mode: TextParseMode = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getFileMimeType(RootObject):
    __tdlib_type__ = "getFileMimeType"
    file_name: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getFileExtension(RootObject):
    __tdlib_type__ = "getFileExtension"
    mime_type: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class cleanFileName(RootObject):
    __tdlib_type__ = "cleanFileName"
    file_name: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getLanguagePackString(RootObject):
    __tdlib_type__ = "getLanguagePackString"
    language_pack_database_path: str = attr.ib()
    localization_target: str = attr.ib()
    language_pack_id: str = attr.ib()
    key: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getJsonValue(RootObject):
    __tdlib_type__ = "getJsonValue"
    json: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getJsonString(RootObject):
    __tdlib_type__ = "getJsonString"
    json_value: JsonValue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setPollAnswer(RootObject):
    __tdlib_type__ = "setPollAnswer"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    option_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class stopPoll(RootObject):
    __tdlib_type__ = "stopPoll"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    reply_markup: ReplyMarkup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getLoginUrlInfo(RootObject):
    __tdlib_type__ = "getLoginUrlInfo"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    button_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getLoginUrl(RootObject):
    __tdlib_type__ = "getLoginUrl"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    button_id: int = attr.ib()
    allow_write_access: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getInlineQueryResults(RootObject):
    __tdlib_type__ = "getInlineQueryResults"
    bot_user_id: int = attr.ib()
    chat_id: int = attr.ib()
    user_location: location = attr.ib()
    query: str = attr.ib()
    offset: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class answerInlineQuery(RootObject):
    __tdlib_type__ = "answerInlineQuery"
    inline_query_id: int = attr.ib()
    is_personal: bool = attr.ib()
    results: typing.Sequence[InputInlineQueryResult] = attr.ib()
    cache_time: int = attr.ib()
    next_offset: str = attr.ib()
    switch_pm_text: str = attr.ib()
    switch_pm_parameter: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getCallbackQueryAnswer(RootObject):
    __tdlib_type__ = "getCallbackQueryAnswer"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    payload: CallbackQueryPayload = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class answerCallbackQuery(RootObject):
    __tdlib_type__ = "answerCallbackQuery"
    callback_query_id: int = attr.ib()
    text: str = attr.ib()
    show_alert: bool = attr.ib()
    url: str = attr.ib()
    cache_time: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class answerShippingQuery(RootObject):
    __tdlib_type__ = "answerShippingQuery"
    shipping_query_id: int = attr.ib()
    shipping_options: typing.Sequence[shippingOption] = attr.ib()
    error_message: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class answerPreCheckoutQuery(RootObject):
    __tdlib_type__ = "answerPreCheckoutQuery"
    pre_checkout_query_id: int = attr.ib()
    error_message: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setGameScore(RootObject):
    __tdlib_type__ = "setGameScore"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    edit_message: bool = attr.ib()
    user_id: int = attr.ib()
    score: int = attr.ib()
    force: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setInlineGameScore(RootObject):
    __tdlib_type__ = "setInlineGameScore"
    inline_message_id: str = attr.ib()
    edit_message: bool = attr.ib()
    user_id: int = attr.ib()
    score: int = attr.ib()
    force: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getGameHighScores(RootObject):
    __tdlib_type__ = "getGameHighScores"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getInlineGameHighScores(RootObject):
    __tdlib_type__ = "getInlineGameHighScores"
    inline_message_id: str = attr.ib()
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deleteChatReplyMarkup(RootObject):
    __tdlib_type__ = "deleteChatReplyMarkup"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendChatAction(RootObject):
    __tdlib_type__ = "sendChatAction"
    chat_id: int = attr.ib()
    action: ChatAction = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class openChat(RootObject):
    __tdlib_type__ = "openChat"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class closeChat(RootObject):
    __tdlib_type__ = "closeChat"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class viewMessages(RootObject):
    __tdlib_type__ = "viewMessages"
    chat_id: int = attr.ib()
    message_ids: typing.Sequence[int] = attr.ib()
    force_read: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class openMessageContent(RootObject):
    __tdlib_type__ = "openMessageContent"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class readAllChatMentions(RootObject):
    __tdlib_type__ = "readAllChatMentions"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class createPrivateChat(RootObject):
    __tdlib_type__ = "createPrivateChat"
    user_id: int = attr.ib()
    force: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class createBasicGroupChat(RootObject):
    __tdlib_type__ = "createBasicGroupChat"
    basic_group_id: int = attr.ib()
    force: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class createSupergroupChat(RootObject):
    __tdlib_type__ = "createSupergroupChat"
    supergroup_id: int = attr.ib()
    force: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class createSecretChat(RootObject):
    __tdlib_type__ = "createSecretChat"
    secret_chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class createNewBasicGroupChat(RootObject):
    __tdlib_type__ = "createNewBasicGroupChat"
    user_ids: typing.Sequence[int] = attr.ib()
    title: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class createNewSupergroupChat(RootObject):
    __tdlib_type__ = "createNewSupergroupChat"
    title: str = attr.ib()
    is_channel: bool = attr.ib()
    description: str = attr.ib()
    location: chatLocation = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class createNewSecretChat(RootObject):
    __tdlib_type__ = "createNewSecretChat"
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class upgradeBasicGroupChatToSupergroupChat(RootObject):
    __tdlib_type__ = "upgradeBasicGroupChatToSupergroupChat"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setChatChatList(RootObject):
    __tdlib_type__ = "setChatChatList"
    chat_id: int = attr.ib()
    chat_list: ChatList = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setChatTitle(RootObject):
    __tdlib_type__ = "setChatTitle"
    chat_id: int = attr.ib()
    title: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setChatPhoto(RootObject):
    __tdlib_type__ = "setChatPhoto"
    chat_id: int = attr.ib()
    photo: InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setChatPermissions(RootObject):
    __tdlib_type__ = "setChatPermissions"
    chat_id: int = attr.ib()
    permissions: chatPermissions = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setChatDraftMessage(RootObject):
    __tdlib_type__ = "setChatDraftMessage"
    chat_id: int = attr.ib()
    draft_message: draftMessage = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setChatNotificationSettings(RootObject):
    __tdlib_type__ = "setChatNotificationSettings"
    chat_id: int = attr.ib()
    notification_settings: chatNotificationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class toggleChatIsPinned(RootObject):
    __tdlib_type__ = "toggleChatIsPinned"
    chat_id: int = attr.ib()
    is_pinned: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class toggleChatIsMarkedAsUnread(RootObject):
    __tdlib_type__ = "toggleChatIsMarkedAsUnread"
    chat_id: int = attr.ib()
    is_marked_as_unread: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class toggleChatDefaultDisableNotification(RootObject):
    __tdlib_type__ = "toggleChatDefaultDisableNotification"
    chat_id: int = attr.ib()
    default_disable_notification: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setChatClientData(RootObject):
    __tdlib_type__ = "setChatClientData"
    chat_id: int = attr.ib()
    client_data: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setChatDescription(RootObject):
    __tdlib_type__ = "setChatDescription"
    chat_id: int = attr.ib()
    description: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setChatDiscussionGroup(RootObject):
    __tdlib_type__ = "setChatDiscussionGroup"
    chat_id: int = attr.ib()
    discussion_chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setChatLocation(RootObject):
    __tdlib_type__ = "setChatLocation"
    chat_id: int = attr.ib()
    location: chatLocation = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setChatSlowModeDelay(RootObject):
    __tdlib_type__ = "setChatSlowModeDelay"
    chat_id: int = attr.ib()
    slow_mode_delay: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pinChatMessage(RootObject):
    __tdlib_type__ = "pinChatMessage"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    disable_notification: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class unpinChatMessage(RootObject):
    __tdlib_type__ = "unpinChatMessage"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class joinChat(RootObject):
    __tdlib_type__ = "joinChat"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class leaveChat(RootObject):
    __tdlib_type__ = "leaveChat"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class addChatMember(RootObject):
    __tdlib_type__ = "addChatMember"
    chat_id: int = attr.ib()
    user_id: int = attr.ib()
    forward_limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class addChatMembers(RootObject):
    __tdlib_type__ = "addChatMembers"
    chat_id: int = attr.ib()
    user_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setChatMemberStatus(RootObject):
    __tdlib_type__ = "setChatMemberStatus"
    chat_id: int = attr.ib()
    user_id: int = attr.ib()
    status: ChatMemberStatus = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class canTransferOwnership(RootObject):
    __tdlib_type__ = "canTransferOwnership"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class transferChatOwnership(RootObject):
    __tdlib_type__ = "transferChatOwnership"
    chat_id: int = attr.ib()
    user_id: int = attr.ib()
    password: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getChatMember(RootObject):
    __tdlib_type__ = "getChatMember"
    chat_id: int = attr.ib()
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchChatMembers(RootObject):
    __tdlib_type__ = "searchChatMembers"
    chat_id: int = attr.ib()
    query: str = attr.ib()
    limit: int = attr.ib()
    filter: ChatMembersFilter = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getChatAdministrators(RootObject):
    __tdlib_type__ = "getChatAdministrators"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class clearAllDraftMessages(RootObject):
    __tdlib_type__ = "clearAllDraftMessages"
    exclude_secret_chats: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getChatNotificationSettingsExceptions(RootObject):
    __tdlib_type__ = "getChatNotificationSettingsExceptions"
    scope: NotificationSettingsScope = attr.ib()
    compare_sound: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getScopeNotificationSettings(RootObject):
    __tdlib_type__ = "getScopeNotificationSettings"
    scope: NotificationSettingsScope = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setScopeNotificationSettings(RootObject):
    __tdlib_type__ = "setScopeNotificationSettings"
    scope: NotificationSettingsScope = attr.ib()
    notification_settings: scopeNotificationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class resetAllNotificationSettings(RootObject):
    __tdlib_type__ = "resetAllNotificationSettings"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setPinnedChats(RootObject):
    __tdlib_type__ = "setPinnedChats"
    chat_list: ChatList = attr.ib()
    chat_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class downloadFile(RootObject):
    __tdlib_type__ = "downloadFile"
    file_id: int = attr.ib()
    priority: int = attr.ib()
    offset: int = attr.ib()
    limit: int = attr.ib()
    synchronous: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getFileDownloadedPrefixSize(RootObject):
    __tdlib_type__ = "getFileDownloadedPrefixSize"
    file_id: int = attr.ib()
    offset: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class cancelDownloadFile(RootObject):
    __tdlib_type__ = "cancelDownloadFile"
    file_id: int = attr.ib()
    only_if_pending: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class uploadFile(RootObject):
    __tdlib_type__ = "uploadFile"
    file: InputFile = attr.ib()
    file_type: FileType = attr.ib()
    priority: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class cancelUploadFile(RootObject):
    __tdlib_type__ = "cancelUploadFile"
    file_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class writeGeneratedFilePart(RootObject):
    __tdlib_type__ = "writeGeneratedFilePart"
    generation_id: int = attr.ib()
    offset: int = attr.ib()
    data: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setFileGenerationProgress(RootObject):
    __tdlib_type__ = "setFileGenerationProgress"
    generation_id: int = attr.ib()
    expected_size: int = attr.ib()
    local_prefix_size: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class finishFileGeneration(RootObject):
    __tdlib_type__ = "finishFileGeneration"
    generation_id: int = attr.ib()
    error: error = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class readFilePart(RootObject):
    __tdlib_type__ = "readFilePart"
    file_id: int = attr.ib()
    offset: int = attr.ib()
    count: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deleteFile(RootObject):
    __tdlib_type__ = "deleteFile"
    file_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class generateChatInviteLink(RootObject):
    __tdlib_type__ = "generateChatInviteLink"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkChatInviteLink(RootObject):
    __tdlib_type__ = "checkChatInviteLink"
    invite_link: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class joinChatByInviteLink(RootObject):
    __tdlib_type__ = "joinChatByInviteLink"
    invite_link: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class createCall(RootObject):
    __tdlib_type__ = "createCall"
    user_id: int = attr.ib()
    protocol: callProtocol = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class acceptCall(RootObject):
    __tdlib_type__ = "acceptCall"
    call_id: int = attr.ib()
    protocol: callProtocol = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class discardCall(RootObject):
    __tdlib_type__ = "discardCall"
    call_id: int = attr.ib()
    is_disconnected: bool = attr.ib()
    duration: int = attr.ib()
    connection_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendCallRating(RootObject):
    __tdlib_type__ = "sendCallRating"
    call_id: int = attr.ib()
    rating: int = attr.ib()
    comment: str = attr.ib()
    problems: typing.Sequence[CallProblem] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendCallDebugInformation(RootObject):
    __tdlib_type__ = "sendCallDebugInformation"
    call_id: int = attr.ib()
    debug_information: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class blockUser(RootObject):
    __tdlib_type__ = "blockUser"
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class unblockUser(RootObject):
    __tdlib_type__ = "unblockUser"
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getBlockedUsers(RootObject):
    __tdlib_type__ = "getBlockedUsers"
    offset: int = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class addContact(RootObject):
    __tdlib_type__ = "addContact"
    contact: contact = attr.ib()
    share_phone_number: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class importContacts(RootObject):
    __tdlib_type__ = "importContacts"
    contacts: typing.Sequence[contact] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getContacts(RootObject):
    __tdlib_type__ = "getContacts"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchContacts(RootObject):
    __tdlib_type__ = "searchContacts"
    query: str = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class removeContacts(RootObject):
    __tdlib_type__ = "removeContacts"
    user_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getImportedContactCount(RootObject):
    __tdlib_type__ = "getImportedContactCount"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class changeImportedContacts(RootObject):
    __tdlib_type__ = "changeImportedContacts"
    contacts: typing.Sequence[contact] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class clearImportedContacts(RootObject):
    __tdlib_type__ = "clearImportedContacts"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sharePhoneNumber(RootObject):
    __tdlib_type__ = "sharePhoneNumber"
    user_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getUserProfilePhotos(RootObject):
    __tdlib_type__ = "getUserProfilePhotos"
    user_id: int = attr.ib()
    offset: int = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getStickers(RootObject):
    __tdlib_type__ = "getStickers"
    emoji: str = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchStickers(RootObject):
    __tdlib_type__ = "searchStickers"
    emoji: str = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getInstalledStickerSets(RootObject):
    __tdlib_type__ = "getInstalledStickerSets"
    is_masks: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getArchivedStickerSets(RootObject):
    __tdlib_type__ = "getArchivedStickerSets"
    is_masks: bool = attr.ib()
    offset_sticker_set_id: int = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getTrendingStickerSets(RootObject):
    __tdlib_type__ = "getTrendingStickerSets"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getAttachedStickerSets(RootObject):
    __tdlib_type__ = "getAttachedStickerSets"
    file_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getStickerSet(RootObject):
    __tdlib_type__ = "getStickerSet"
    set_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchStickerSet(RootObject):
    __tdlib_type__ = "searchStickerSet"
    name: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchInstalledStickerSets(RootObject):
    __tdlib_type__ = "searchInstalledStickerSets"
    is_masks: bool = attr.ib()
    query: str = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchStickerSets(RootObject):
    __tdlib_type__ = "searchStickerSets"
    query: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class changeStickerSet(RootObject):
    __tdlib_type__ = "changeStickerSet"
    set_id: int = attr.ib()
    is_installed: bool = attr.ib()
    is_archived: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class viewTrendingStickerSets(RootObject):
    __tdlib_type__ = "viewTrendingStickerSets"
    sticker_set_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class reorderInstalledStickerSets(RootObject):
    __tdlib_type__ = "reorderInstalledStickerSets"
    is_masks: bool = attr.ib()
    sticker_set_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getRecentStickers(RootObject):
    __tdlib_type__ = "getRecentStickers"
    is_attached: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class addRecentSticker(RootObject):
    __tdlib_type__ = "addRecentSticker"
    is_attached: bool = attr.ib()
    sticker: InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class removeRecentSticker(RootObject):
    __tdlib_type__ = "removeRecentSticker"
    is_attached: bool = attr.ib()
    sticker: InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class clearRecentStickers(RootObject):
    __tdlib_type__ = "clearRecentStickers"
    is_attached: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getFavoriteStickers(RootObject):
    __tdlib_type__ = "getFavoriteStickers"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class addFavoriteSticker(RootObject):
    __tdlib_type__ = "addFavoriteSticker"
    sticker: InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class removeFavoriteSticker(RootObject):
    __tdlib_type__ = "removeFavoriteSticker"
    sticker: InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getStickerEmojis(RootObject):
    __tdlib_type__ = "getStickerEmojis"
    sticker: InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchEmojis(RootObject):
    __tdlib_type__ = "searchEmojis"
    text: str = attr.ib()
    exact_match: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getEmojiSuggestionsUrl(RootObject):
    __tdlib_type__ = "getEmojiSuggestionsUrl"
    language_code: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getSavedAnimations(RootObject):
    __tdlib_type__ = "getSavedAnimations"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class addSavedAnimation(RootObject):
    __tdlib_type__ = "addSavedAnimation"
    animation: InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class removeSavedAnimation(RootObject):
    __tdlib_type__ = "removeSavedAnimation"
    animation: InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getRecentInlineBots(RootObject):
    __tdlib_type__ = "getRecentInlineBots"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchHashtags(RootObject):
    __tdlib_type__ = "searchHashtags"
    prefix: str = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class removeRecentHashtag(RootObject):
    __tdlib_type__ = "removeRecentHashtag"
    hashtag: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getWebPagePreview(RootObject):
    __tdlib_type__ = "getWebPagePreview"
    text: formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getWebPageInstantView(RootObject):
    __tdlib_type__ = "getWebPageInstantView"
    url: str = attr.ib()
    force_full: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setProfilePhoto(RootObject):
    __tdlib_type__ = "setProfilePhoto"
    photo: InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deleteProfilePhoto(RootObject):
    __tdlib_type__ = "deleteProfilePhoto"
    profile_photo_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setName(RootObject):
    __tdlib_type__ = "setName"
    first_name: str = attr.ib()
    last_name: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setBio(RootObject):
    __tdlib_type__ = "setBio"
    bio: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setUsername(RootObject):
    __tdlib_type__ = "setUsername"
    username: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class changePhoneNumber(RootObject):
    __tdlib_type__ = "changePhoneNumber"
    phone_number: str = attr.ib()
    settings: phoneNumberAuthenticationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class resendChangePhoneNumberCode(RootObject):
    __tdlib_type__ = "resendChangePhoneNumberCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkChangePhoneNumberCode(RootObject):
    __tdlib_type__ = "checkChangePhoneNumberCode"
    code: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getActiveSessions(RootObject):
    __tdlib_type__ = "getActiveSessions"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class terminateSession(RootObject):
    __tdlib_type__ = "terminateSession"
    session_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class terminateAllOtherSessions(RootObject):
    __tdlib_type__ = "terminateAllOtherSessions"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getConnectedWebsites(RootObject):
    __tdlib_type__ = "getConnectedWebsites"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class disconnectWebsite(RootObject):
    __tdlib_type__ = "disconnectWebsite"
    website_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class disconnectAllWebsites(RootObject):
    __tdlib_type__ = "disconnectAllWebsites"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setSupergroupUsername(RootObject):
    __tdlib_type__ = "setSupergroupUsername"
    supergroup_id: int = attr.ib()
    username: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setSupergroupStickerSet(RootObject):
    __tdlib_type__ = "setSupergroupStickerSet"
    supergroup_id: int = attr.ib()
    sticker_set_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class toggleSupergroupSignMessages(RootObject):
    __tdlib_type__ = "toggleSupergroupSignMessages"
    supergroup_id: int = attr.ib()
    sign_messages: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class toggleSupergroupIsAllHistoryAvailable(RootObject):
    __tdlib_type__ = "toggleSupergroupIsAllHistoryAvailable"
    supergroup_id: int = attr.ib()
    is_all_history_available: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class reportSupergroupSpam(RootObject):
    __tdlib_type__ = "reportSupergroupSpam"
    supergroup_id: int = attr.ib()
    user_id: int = attr.ib()
    message_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getSupergroupMembers(RootObject):
    __tdlib_type__ = "getSupergroupMembers"
    supergroup_id: int = attr.ib()
    filter: SupergroupMembersFilter = attr.ib()
    offset: int = attr.ib()
    limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deleteSupergroup(RootObject):
    __tdlib_type__ = "deleteSupergroup"
    supergroup_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class closeSecretChat(RootObject):
    __tdlib_type__ = "closeSecretChat"
    secret_chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getChatEventLog(RootObject):
    __tdlib_type__ = "getChatEventLog"
    chat_id: int = attr.ib()
    query: str = attr.ib()
    from_event_id: int = attr.ib()
    limit: int = attr.ib()
    filters: chatEventLogFilters = attr.ib()
    user_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getPaymentForm(RootObject):
    __tdlib_type__ = "getPaymentForm"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class validateOrderInfo(RootObject):
    __tdlib_type__ = "validateOrderInfo"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    order_info: orderInfo = attr.ib()
    allow_save: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendPaymentForm(RootObject):
    __tdlib_type__ = "sendPaymentForm"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()
    order_info_id: str = attr.ib()
    shipping_option_id: str = attr.ib()
    credentials: InputCredentials = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getPaymentReceipt(RootObject):
    __tdlib_type__ = "getPaymentReceipt"
    chat_id: int = attr.ib()
    message_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getSavedOrderInfo(RootObject):
    __tdlib_type__ = "getSavedOrderInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deleteSavedOrderInfo(RootObject):
    __tdlib_type__ = "deleteSavedOrderInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deleteSavedCredentials(RootObject):
    __tdlib_type__ = "deleteSavedCredentials"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getSupportUser(RootObject):
    __tdlib_type__ = "getSupportUser"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getBackgrounds(RootObject):
    __tdlib_type__ = "getBackgrounds"
    for_dark_theme: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getBackgroundUrl(RootObject):
    __tdlib_type__ = "getBackgroundUrl"
    name: str = attr.ib()
    type: BackgroundType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class searchBackground(RootObject):
    __tdlib_type__ = "searchBackground"
    name: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setBackground(RootObject):
    __tdlib_type__ = "setBackground"
    background: InputBackground = attr.ib()
    type: BackgroundType = attr.ib()
    for_dark_theme: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class removeBackground(RootObject):
    __tdlib_type__ = "removeBackground"
    background_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class resetBackgrounds(RootObject):
    __tdlib_type__ = "resetBackgrounds"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getLocalizationTargetInfo(RootObject):
    __tdlib_type__ = "getLocalizationTargetInfo"
    only_local: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getLanguagePackInfo(RootObject):
    __tdlib_type__ = "getLanguagePackInfo"
    language_pack_id: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getLanguagePackStrings(RootObject):
    __tdlib_type__ = "getLanguagePackStrings"
    language_pack_id: str = attr.ib()
    keys: typing.Sequence[str] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class synchronizeLanguagePack(RootObject):
    __tdlib_type__ = "synchronizeLanguagePack"
    language_pack_id: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class addCustomServerLanguagePack(RootObject):
    __tdlib_type__ = "addCustomServerLanguagePack"
    language_pack_id: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setCustomLanguagePack(RootObject):
    __tdlib_type__ = "setCustomLanguagePack"
    info: languagePackInfo = attr.ib()
    strings: typing.Sequence[languagePackString] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class editCustomLanguagePackInfo(RootObject):
    __tdlib_type__ = "editCustomLanguagePackInfo"
    info: languagePackInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setCustomLanguagePackString(RootObject):
    __tdlib_type__ = "setCustomLanguagePackString"
    language_pack_id: str = attr.ib()
    new_string: languagePackString = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deleteLanguagePack(RootObject):
    __tdlib_type__ = "deleteLanguagePack"
    language_pack_id: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class registerDevice(RootObject):
    __tdlib_type__ = "registerDevice"
    device_token: DeviceToken = attr.ib()
    other_user_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class processPushNotification(RootObject):
    __tdlib_type__ = "processPushNotification"
    payload: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getPushReceiverId(RootObject):
    __tdlib_type__ = "getPushReceiverId"
    payload: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getRecentlyVisitedTMeUrls(RootObject):
    __tdlib_type__ = "getRecentlyVisitedTMeUrls"
    referrer: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setUserPrivacySettingRules(RootObject):
    __tdlib_type__ = "setUserPrivacySettingRules"
    setting: UserPrivacySetting = attr.ib()
    rules: userPrivacySettingRules = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getUserPrivacySettingRules(RootObject):
    __tdlib_type__ = "getUserPrivacySettingRules"
    setting: UserPrivacySetting = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getOption(RootObject):
    __tdlib_type__ = "getOption"
    name: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setOption(RootObject):
    __tdlib_type__ = "setOption"
    name: str = attr.ib()
    value: OptionValue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setAccountTtl(RootObject):
    __tdlib_type__ = "setAccountTtl"
    ttl: accountTtl = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getAccountTtl(RootObject):
    __tdlib_type__ = "getAccountTtl"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deleteAccount(RootObject):
    __tdlib_type__ = "deleteAccount"
    reason: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class removeChatActionBar(RootObject):
    __tdlib_type__ = "removeChatActionBar"
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class reportChat(RootObject):
    __tdlib_type__ = "reportChat"
    chat_id: int = attr.ib()
    reason: ChatReportReason = attr.ib()
    message_ids: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getChatStatisticsUrl(RootObject):
    __tdlib_type__ = "getChatStatisticsUrl"
    chat_id: int = attr.ib()
    parameters: str = attr.ib()
    is_dark: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getStorageStatistics(RootObject):
    __tdlib_type__ = "getStorageStatistics"
    chat_limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getStorageStatisticsFast(RootObject):
    __tdlib_type__ = "getStorageStatisticsFast"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getDatabaseStatistics(RootObject):
    __tdlib_type__ = "getDatabaseStatistics"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class optimizeStorage(RootObject):
    __tdlib_type__ = "optimizeStorage"
    size: int = attr.ib()
    ttl: int = attr.ib()
    count: int = attr.ib()
    immunity_delay: int = attr.ib()
    file_types: typing.Sequence[FileType] = attr.ib()
    chat_ids: typing.Sequence[int] = attr.ib()
    exclude_chat_ids: typing.Sequence[int] = attr.ib()
    chat_limit: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setNetworkType(RootObject):
    __tdlib_type__ = "setNetworkType"
    type: NetworkType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getNetworkStatistics(RootObject):
    __tdlib_type__ = "getNetworkStatistics"
    only_current: bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class addNetworkStatistics(RootObject):
    __tdlib_type__ = "addNetworkStatistics"
    entry: NetworkStatisticsEntry = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class resetNetworkStatistics(RootObject):
    __tdlib_type__ = "resetNetworkStatistics"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getAutoDownloadSettingsPresets(RootObject):
    __tdlib_type__ = "getAutoDownloadSettingsPresets"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setAutoDownloadSettings(RootObject):
    __tdlib_type__ = "setAutoDownloadSettings"
    settings: autoDownloadSettings = attr.ib()
    type: NetworkType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getPassportElement(RootObject):
    __tdlib_type__ = "getPassportElement"
    type: PassportElementType = attr.ib()
    password: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getAllPassportElements(RootObject):
    __tdlib_type__ = "getAllPassportElements"
    password: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setPassportElement(RootObject):
    __tdlib_type__ = "setPassportElement"
    element: InputPassportElement = attr.ib()
    password: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class deletePassportElement(RootObject):
    __tdlib_type__ = "deletePassportElement"
    type: PassportElementType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setPassportElementErrors(RootObject):
    __tdlib_type__ = "setPassportElementErrors"
    user_id: int = attr.ib()
    errors: typing.Sequence[inputPassportElementError] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getPreferredCountryLanguage(RootObject):
    __tdlib_type__ = "getPreferredCountryLanguage"
    country_code: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendPhoneNumberVerificationCode(RootObject):
    __tdlib_type__ = "sendPhoneNumberVerificationCode"
    phone_number: str = attr.ib()
    settings: phoneNumberAuthenticationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class resendPhoneNumberVerificationCode(RootObject):
    __tdlib_type__ = "resendPhoneNumberVerificationCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkPhoneNumberVerificationCode(RootObject):
    __tdlib_type__ = "checkPhoneNumberVerificationCode"
    code: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendEmailAddressVerificationCode(RootObject):
    __tdlib_type__ = "sendEmailAddressVerificationCode"
    email_address: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class resendEmailAddressVerificationCode(RootObject):
    __tdlib_type__ = "resendEmailAddressVerificationCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkEmailAddressVerificationCode(RootObject):
    __tdlib_type__ = "checkEmailAddressVerificationCode"
    code: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getPassportAuthorizationForm(RootObject):
    __tdlib_type__ = "getPassportAuthorizationForm"
    bot_user_id: int = attr.ib()
    scope: str = attr.ib()
    public_key: str = attr.ib()
    nonce: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getPassportAuthorizationFormAvailableElements(RootObject):
    __tdlib_type__ = "getPassportAuthorizationFormAvailableElements"
    autorization_form_id: int = attr.ib()
    password: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendPassportAuthorizationForm(RootObject):
    __tdlib_type__ = "sendPassportAuthorizationForm"
    autorization_form_id: int = attr.ib()
    types: typing.Sequence[PassportElementType] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendPhoneNumberConfirmationCode(RootObject):
    __tdlib_type__ = "sendPhoneNumberConfirmationCode"
    hash: str = attr.ib()
    phone_number: str = attr.ib()
    settings: phoneNumberAuthenticationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class resendPhoneNumberConfirmationCode(RootObject):
    __tdlib_type__ = "resendPhoneNumberConfirmationCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class checkPhoneNumberConfirmationCode(RootObject):
    __tdlib_type__ = "checkPhoneNumberConfirmationCode"
    code: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setBotUpdatesStatus(RootObject):
    __tdlib_type__ = "setBotUpdatesStatus"
    pending_update_count: int = attr.ib()
    error_message: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class uploadStickerFile(RootObject):
    __tdlib_type__ = "uploadStickerFile"
    user_id: int = attr.ib()
    png_sticker: InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class createNewStickerSet(RootObject):
    __tdlib_type__ = "createNewStickerSet"
    user_id: int = attr.ib()
    title: str = attr.ib()
    name: str = attr.ib()
    is_masks: bool = attr.ib()
    stickers: typing.Sequence[inputSticker] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class addStickerToSet(RootObject):
    __tdlib_type__ = "addStickerToSet"
    user_id: int = attr.ib()
    name: str = attr.ib()
    sticker: inputSticker = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setStickerPositionInSet(RootObject):
    __tdlib_type__ = "setStickerPositionInSet"
    sticker: InputFile = attr.ib()
    position: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class removeStickerFromSet(RootObject):
    __tdlib_type__ = "removeStickerFromSet"
    sticker: InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getMapThumbnailFile(RootObject):
    __tdlib_type__ = "getMapThumbnailFile"
    location: location = attr.ib()
    zoom: int = attr.ib()
    width: int = attr.ib()
    height: int = attr.ib()
    scale: int = attr.ib()
    chat_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class acceptTermsOfService(RootObject):
    __tdlib_type__ = "acceptTermsOfService"
    terms_of_service_id: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendCustomRequest(RootObject):
    __tdlib_type__ = "sendCustomRequest"
    method: str = attr.ib()
    parameters: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class answerCustomQuery(RootObject):
    __tdlib_type__ = "answerCustomQuery"
    custom_query_id: int = attr.ib()
    data: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class sendTonLiteServerRequest(RootObject):
    __tdlib_type__ = "sendTonLiteServerRequest"
    request: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getTonWalletPasswordSalt(RootObject):
    __tdlib_type__ = "getTonWalletPasswordSalt"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setAlarm(RootObject):
    __tdlib_type__ = "setAlarm"
    seconds: decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getCountryCode(RootObject):
    __tdlib_type__ = "getCountryCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getInviteText(RootObject):
    __tdlib_type__ = "getInviteText"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getDeepLinkInfo(RootObject):
    __tdlib_type__ = "getDeepLinkInfo"
    link: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getApplicationConfig(RootObject):
    __tdlib_type__ = "getApplicationConfig"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class saveApplicationLogEvent(RootObject):
    __tdlib_type__ = "saveApplicationLogEvent"
    type: str = attr.ib()
    chat_id: int = attr.ib()
    data: JsonValue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class addProxy(RootObject):
    __tdlib_type__ = "addProxy"
    server: str = attr.ib()
    port: int = attr.ib()
    enable: bool = attr.ib()
    type: ProxyType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class editProxy(RootObject):
    __tdlib_type__ = "editProxy"
    proxy_id: int = attr.ib()
    server: str = attr.ib()
    port: int = attr.ib()
    enable: bool = attr.ib()
    type: ProxyType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class enableProxy(RootObject):
    __tdlib_type__ = "enableProxy"
    proxy_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class disableProxy(RootObject):
    __tdlib_type__ = "disableProxy"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class removeProxy(RootObject):
    __tdlib_type__ = "removeProxy"
    proxy_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getProxies(RootObject):
    __tdlib_type__ = "getProxies"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getProxyLink(RootObject):
    __tdlib_type__ = "getProxyLink"
    proxy_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class pingProxy(RootObject):
    __tdlib_type__ = "pingProxy"
    proxy_id: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setLogStream(RootObject):
    __tdlib_type__ = "setLogStream"
    log_stream: LogStream = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getLogStream(RootObject):
    __tdlib_type__ = "getLogStream"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setLogVerbosityLevel(RootObject):
    __tdlib_type__ = "setLogVerbosityLevel"
    new_verbosity_level: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getLogVerbosityLevel(RootObject):
    __tdlib_type__ = "getLogVerbosityLevel"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getLogTags(RootObject):
    __tdlib_type__ = "getLogTags"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class setLogTagVerbosityLevel(RootObject):
    __tdlib_type__ = "setLogTagVerbosityLevel"
    tag: str = attr.ib()
    new_verbosity_level: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class getLogTagVerbosityLevel(RootObject):
    __tdlib_type__ = "getLogTagVerbosityLevel"
    tag: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class addLogMessage(RootObject):
    __tdlib_type__ = "addLogMessage"
    verbosity_level: int = attr.ib()
    text: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testCallEmpty(RootObject):
    __tdlib_type__ = "testCallEmpty"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testCallString(RootObject):
    __tdlib_type__ = "testCallString"
    x: str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testCallBytes(RootObject):
    __tdlib_type__ = "testCallBytes"
    x: bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testCallVectorInt(RootObject):
    __tdlib_type__ = "testCallVectorInt"
    x: typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testCallVectorIntObject(RootObject):
    __tdlib_type__ = "testCallVectorIntObject"
    x: typing.Sequence[testInt] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testCallVectorString(RootObject):
    __tdlib_type__ = "testCallVectorString"
    x: typing.Sequence[str] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testCallVectorStringObject(RootObject):
    __tdlib_type__ = "testCallVectorStringObject"
    x: typing.Sequence[testString] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testSquareInt(RootObject):
    __tdlib_type__ = "testSquareInt"
    x: int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testNetwork(RootObject):
    __tdlib_type__ = "testNetwork"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testProxy(RootObject):
    __tdlib_type__ = "testProxy"
    server: str = attr.ib()
    port: int = attr.ib()
    type: ProxyType = attr.ib()
    dc_id: int = attr.ib()
    timeout: decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testGetDifference(RootObject):
    __tdlib_type__ = "testGetDifference"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testUseUpdate(RootObject):
    __tdlib_type__ = "testUseUpdate"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class testReturnError(RootObject):
    __tdlib_type__ = "testReturnError"
    error: error = attr.ib()


# use these when you need to use `typing.get_type_hints` or `eval`
# to resolve a string representation of these types
tdlib_gen_globals = globals()
tdlib_gen_locals = locals()
