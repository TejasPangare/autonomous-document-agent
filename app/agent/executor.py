from app.tools.document_tool import DocumentTool
from app.tools.reviewer_tool import ReviewerTool
from app.tools.writer_tool import WriterTool


class Executor:

    def __init__(self):

        self.writer = WriterTool()

        self.document_tool = DocumentTool()
        
        self.reviewer = ReviewerTool()

    def execute(self, request, plan):

        generated_document = self.writer.execute(
        request=request,
        plan=plan
        )

        generated_document = self.reviewer.review(
            generated_document
        )

        path = self.document_tool.generate(
            generated_document
        )

        return {
            "document": generated_document,
            "path": path
        }