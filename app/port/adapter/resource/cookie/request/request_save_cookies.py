from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class RequestSaveCookies(BaseModel):
    class Cookie(BaseModel):
        """https://developer.mozilla.org/ja/docs/Web/HTTP/Cookies"""

        domain: str = Field(title='ドメイン名', description='Domain 属性は、Cookie を受信することができるホストを指定します。'
                                                       '指定されていない場合は、既定で Cookie を設定したのと同じホストとなり、'
                                                       'サブドメインは除外されます。 Domain が指定された場合、サブドメインは常に'
                                                       '含まれます。したがって、 Domain を指定すると省略時よりも制限が緩和されます。'
                                                       'ただし、サブドメイン間でユーザーに関する情報を共有する場合は有用になるでしょう。')
        path: str = Field(title='パス', description='Path 属性は、 Cookie ヘッダーを送信するためにリクエストされた URL の中に含む'
                                                  '必要がある URL のパスを示します。 %x2F ("/") の文字はディレクトリー区切り文字と'
                                                  'して解釈され、サブディレクトリーにも同様に一致します。')
        name: str = Field(title='クッキー名')
        value: str = Field(title='クッキーの値')

    organization_id: str = Field(title='組織ID')
    cookies: List[RequestSaveCookies.Cookie] = Field(title='クッキー一覧')
