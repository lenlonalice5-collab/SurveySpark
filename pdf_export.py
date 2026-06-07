from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


pdfmetrics.registerFont(
    TTFont(
        "YaHei",
        r"C:\Windows\Fonts\msyh.ttc"
    )
)


def export_pdf(
    report_text,
    stats_text,
    duration_text
):

    pdf = SimpleDocTemplate(
        "Interview_Report.pdf"
    )

    styles = getSampleStyleSheet()

    styles["Title"].fontName = "YaHei"
    styles["BodyText"].fontName = "YaHei"
    styles["Heading2"].fontName = "YaHei"

    content = []

    content.append(
        Paragraph(
            "InterviewGPT AI面试报告",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1,20)
    )

    content.append(
        Paragraph(
            f"面试时长：{duration_text}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1,10)
    )

    content.append(
        Paragraph(
            "面试统计",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            stats_text.replace("\n","<br/>"),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1,20)
    )

    content.append(
        Paragraph(
            "能力画像",
            styles["Heading2"]
        )
    )

    content.append(
        Image(
            "radar_chart.png",
            width=300,
            height=300
        )
    )

    content.append(
        Spacer(1,20)
    )

    content.append(
        Paragraph(
            "AI面试报告",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            report_text.replace("\n","<br/>"),
            styles["BodyText"]
        )
    )

    pdf.build(content)

    return "Interview_Report.pdf"