NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

from .nodes import CopyFileToCustomDir

NODE_CLASS_MAPPINGS["CopyFileToCustomDir"] = CopyFileToCustomDir
NODE_DISPLAY_NAME_MAPPINGS["CopyFileToCustomDir"] = "将文件复制到自定义目录"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]