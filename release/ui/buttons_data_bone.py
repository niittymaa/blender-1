
import bpy
 
class BoneButtonsPanel(bpy.types.Panel):
	__space_type__ = "BUTTONS_WINDOW"
	__region_type__ = "WINDOW"
	__context__ = "bone"
	
	def poll(self, context):
		return (context.bone or context.edit_bone)

class BONE_PT_context_bone(BoneButtonsPanel):
	__idname__ = "BONE_PT_context_bone"
	__show_header__ = False

	def draw(self, context):
		layout = self.layout
		bone = context.bone
		if not bone:
			bone = context.edit_bone
		
		row = layout.row()
		row.itemL(text="", icon="ICON_BONE_DATA")
		row.itemR(bone, "name", text="")

class BONE_PT_transform(BoneButtonsPanel):
	__idname__ = "BONE_PT_transform"
	__label__ = "Transform"

	def draw(self, context):
		layout = self.layout
		ob = context.object
		bone = context.bone

		if not bone:
			bone = context.edit_bone

			row = layout.row()
			row.column().itemR(bone, "head")
			row.column().itemR(bone, "tail")

			col = row.column()
			sub = col.column(align=True)
			sub.itemL(text="Roll:")
			sub.itemR(bone, "roll", text="")
			sub.itemL()
			sub.itemR(bone, "locked")
			sub.itemS()
		else:
			pchan = ob.pose.pose_channels[context.bone.name]

			layout.itemR(pchan, "rotation_mode")

			row = layout.row()
			col = row.column()
			col.itemR(pchan, "location")
			col.active = not (bone.parent and bone.connected)

			col = row.column()
			if pchan.rotation_mode == 'QUATERNION':
				col.itemR(pchan, "rotation", text="Rotation")
			else:
				col.itemR(pchan, "euler_rotation", text="Rotation")

			row.column().itemR(pchan, "scale")

			if pchan.rotation_mode == 'QUATERNION':
				col = layout.column(align=True)
				col.itemL(text="Euler:")
				col.row().itemR(pchan, "euler_rotation", text="")

class BONE_PT_bone(BoneButtonsPanel):
	__idname__ = "BONE_PT_bone"
	__label__ = "Bone"


	def draw(self, context):
		layout = self.layout
		bone = context.bone
		arm = context.armature
		if not bone:
			bone = context.edit_bone

		split = layout.split()

		sub = split.column()
		sub.itemL(text="Parent:")
		if context.bone:
			sub.itemR(bone, "parent", text="")
		else:
			sub.item_pointerR(bone, "parent", arm, "edit_bones", text="")
		row = sub.row()
		row.itemR(bone, "connected")
		row.active = bone.parent != None

		sub.itemL(text="Layers:")
		sub.template_layers(bone, "layer")

		sub = split.column()

		sub.itemL(text="Inherit:")
		sub.itemR(bone, "hinge", text="Rotation")
		sub.itemR(bone, "inherit_scale", text="Scale")
		
		sub.itemL(text="Display:")
		sub.itemR(bone, "draw_wire", text="Wireframe")
		sub.itemR(bone, "hidden", text="Hide")

class BONE_PT_inverse_kinematics(BoneButtonsPanel):
	__idname__ = "BONE_PT_inverse_kinematics"
	__label__ = "Inverse Kinematics"
	__default_closed__ = True
	
	def poll(self, context):
		ob = context.object
		bone = context.bone

		if ob and context.bone:
			pchan = ob.pose.pose_channels[context.bone.name]
			return pchan.has_ik
		
		return False

	def draw(self, context):
		layout = self.layout
		ob = context.object
		bone = context.bone
		pchan = ob.pose.pose_channels[context.bone.name]

		split = layout.split(percentage=0.25)
		split.itemR(pchan, "ik_dof_x", text="X")
		row = split.row()
		row.itemR(pchan, "ik_stiffness_x", text="Stiffness")
		row.active = pchan.ik_dof_x

		split = layout.split(percentage=0.25)
		row = split.row()
		row.itemR(pchan, "ik_limit_x", text="Limit")
		row.active = pchan.ik_dof_x
		row = split.row(align=True)
		row.itemR(pchan, "ik_min_x", text="")
		row.itemR(pchan, "ik_max_x", text="")
		row.active = pchan.ik_dof_x and pchan.ik_limit_x

		split = layout.split(percentage=0.25)
		split.itemR(pchan, "ik_dof_y", text="Y")
		row = split.row()
		row.itemR(pchan, "ik_stiffness_y", text="Stiffness")
		row.active = pchan.ik_dof_y

		split = layout.split(percentage=0.25)
		row = split.row()
		row.itemR(pchan, "ik_limit_y", text="Limit")
		row.active = pchan.ik_dof_y
		row = split.row(align=True)
		row.itemR(pchan, "ik_min_y", text="")
		row.itemR(pchan, "ik_max_y", text="")
		row.active = pchan.ik_dof_y and pchan.ik_limit_y

		split = layout.split(percentage=0.25)
		split.itemR(pchan, "ik_dof_z", text="Z")
		row = split.row()
		row.itemR(pchan, "ik_stiffness_z", text="Stiffness")
		row.active = pchan.ik_dof_z

		split = layout.split(percentage=0.25)
		row = split.row()
		row.itemR(pchan, "ik_limit_z", text="Limit")
		row.active = pchan.ik_dof_z
		row = split.row(align=True)
		row.itemR(pchan, "ik_min_z", text="")
		row.itemR(pchan, "ik_max_z", text="")
		row.active = pchan.ik_dof_z and pchan.ik_limit_z

		split = layout.split()
		split.itemR(pchan, "ik_stretch", text="Stretch")
		split.itemL()

class BONE_PT_deform(BoneButtonsPanel):
	__idname__ = "BONE_PT_deform"
	__label__ = "Deform"
	__default_closed__ = True

	def draw_header(self, context):
		layout = self.layout
		bone = context.bone
		if not bone:
			bone = context.edit_bone
			
		layout.itemR(bone, "deform", text="")

	def draw(self, context):
		layout = self.layout
		bone = context.bone
		if not bone:
			bone = context.edit_bone
	
		layout.active = bone.deform
			
		split = layout.split()

		col = split.column()
		col.itemL(text="Envelope:")
		sub = col.column(align=True)
		sub.itemR(bone, "envelope_distance", text="Distance")
		sub.itemR(bone, "envelope_weight", text="Weight")
		col.itemR(bone, "multiply_vertexgroup_with_envelope", text="Multiply")

		sub = col.column(align=True)
		sub.itemL(text="Radius:")
		sub.itemR(bone, "head_radius", text="Head")
		sub.itemR(bone, "tail_radius", text="Tail")

		col = split.column()
		col.itemL(text="Curved Bones:")
		sub = col.column(align=True)
		sub.itemR(bone, "bbone_segments", text="Segments")
		sub.itemR(bone, "bbone_in", text="Ease In")
		sub.itemR(bone, "bbone_out", text="Ease Out")
		
		col.itemL(text="Offset:")
		col.itemR(bone, "cyclic_offset")

bpy.types.register(BONE_PT_context_bone)
bpy.types.register(BONE_PT_transform)
bpy.types.register(BONE_PT_bone)
bpy.types.register(BONE_PT_deform)
bpy.types.register(BONE_PT_inverse_kinematics)

