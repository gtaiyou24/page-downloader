from __future__ import annotations

from pydantic import BaseModel, Field

from application.page.dpo import DownloadedPageDpo


class DownloadedPageJson(BaseModel):
    url: str = Field(title='URL')
    http_status: int = Field(title='HTTPステータス')
    html: str = Field(title='HTML')
    character_code: str = Field(title='文字コード')

    @staticmethod
    def of(dpo: DownloadedPageDpo) -> DownloadedPageJson:
        return DownloadedPageJson(url=dpo.page.url.value,
                                  http_status=dpo.page.http_status.value,
                                  html=dpo.page.html.text,
                                  character_code=dpo.page.html.character_code.name)
