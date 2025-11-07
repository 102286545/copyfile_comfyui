import os
import shutil
import folder_paths

class CopyFileToCustomDir:
    """将指定文件复制到自定义目标目录"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "source_path": ("STRING", {
                    "default": "models/loras/aaa.sft",
                    "placeholder": "输入源文件路径，例如：models/loras/aaa.sft",
                    "multiline": False
                }),
                "target_dir": ("STRING", {
                    "default": "outputs/",
                    "placeholder": "输入目标目录，例如：outputs/saved_loras/",
                    "multiline": False
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("复制结果",)
    FUNCTION = "copy_file"
    CATEGORY = "文件操作"

    def copy_file(self, source_path, target_dir):
        try:
            # 获取ComfyUI根目录
            comfy_root = os.path.dirname(folder_paths.__file__)
            
            # 处理源文件路径
            if os.path.isabs(source_path):
                source_full = source_path
            else:
                source_full = os.path.join(comfy_root, source_path)
            
            # 验证源文件
            if not os.path.exists(source_full):
                return (f"错误：源文件不存在 - {source_full}",)
            if not os.path.isfile(source_full):
                return (f"错误：源路径不是文件 - {source_full}",)
            
            # 处理目标目录路径
            if os.path.isabs(target_dir):
                target_full = target_dir
            else:
                target_full = os.path.join(comfy_root, target_dir)
            
            # 确保目标目录存在
            os.makedirs(target_full, exist_ok=True)
            
            # 构建目标文件完整路径
            file_name = os.path.basename(source_full)
            dest_path = os.path.join(target_full, file_name)
            
            # 执行复制
            shutil.copy2(source_full, dest_path)
            
            return (f"成功：文件已复制到\n{dest_path}",)
            
        except Exception as e:
            return (f"复制失败：{str(e)}",)

# 注册节点
NODE_CLASS_MAPPINGS = {
    "CopyFileToCustomDir": CopyFileToCustomDir
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CopyFileToCustomDir": "复制文件到自定义目录"
}