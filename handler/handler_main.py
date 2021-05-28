# -*- coding: utf-8 -*-

import g
from sanic import Blueprint
from common.handler import Handler
from common.decorator import auth
from common.get_user import get_user
from common.jwt_func import generate_jwt
from common import util
from biz.biz_user import BizUser
import error

bp_page = Blueprint(name='page', url_prefix='/v1', strict_slashes=True)


@bp_page.route(f'/login', methods=g.SANIC_METHOD.post.value)
@auth()
async def login(r: Handler):
    r_data = r.get_json()
    username = r.get_str('username', data=r_data)
    password = r.get_str('password', data=r_data)

    user_valid_code = r.get_str('valid_code', data=r_data)
    valid_code = r.cookies.get('valid_code')

    if not valid_code:
        return r.error(msg='请重新获取验证码')

    if not user_valid_code:
        return r.param_error(msg='验证码不能为空')

    if user_valid_code.lower() != valid_code.lower():
        return r.error(code=error.ERROR_VALID_ERROR_1008, msg=error.error_code.get('ERROR_VALID_ERROR_1008'))

    if not username or not password:
        return r.param_error(msg='用户名或密码不能为空')
    user = BizUser().get_user_by_username_and_password(username=username, password=password)
    if user:
        # 登录成功
        # 生成jwt返回给前端
        token = generate_jwt(user_id=user.id, user_name=username, user_type=user.user_type)
        return r.success(dict(user_id=user.id, username=username, user_type=user.user_type, token=token))
    else:
        return r.login_error()


@bp_page.route(f'/valid/image', methods=g.SANIC_METHOD.get.value)
@auth()
async def valid_image(r: Handler):
    img = util.get_valid_code_img()
    return r.valid_code_image(valid_code=img.get('valid_code'), image=img.get('img'))


@bp_page.route(f'/user/list', methods=g.SANIC_METHOD.get.value)
@auth()
@get_user([g.PERMISSIONS.teacher.value])
async def user_list(r: Handler):
    page = r.get_int('page', default=1)
    limit = r.get_int('limit', default=10)
    if page < 1:
        page = 1
    if limit < 1:
        limit = 1
    elif limit > 100:
        limit = 100
    data = BizUser().get_user_pagination(offset=(page - 1) * limit, limit=limit)

    return r.success(dict(data=data))


@bp_page.route(f'/user/panel', methods=g.SANIC_METHOD.get.value)
@auth()
@get_user([g.PERMISSIONS.student.value, g.PERMISSIONS.teacher.value])
async def user_panel(r: Handler):
    user_id = r.ctx.user_info['user_id']
    data = BizUser().get_user_by_user_id(user_id=user_id)
    return r.success(dict(user=data))


@bp_page.route(f'/user/insert', methods=g.SANIC_METHOD.post.value)
@auth()
@get_user([g.PERMISSIONS.teacher.value])
async def user_insert(r: Handler):
    r_data = r.get_json()
    username = r.get_str('username', data=r_data)
    password = r.get_str('password', data=r_data)
    equipment = r.get_str('equipment', data=r_data)
    data_tagging = r.get_str('data_tagging', data=r_data)
    model_build = r.get_str('model_build', data=r_data)
    model_check = r.get_str('model_check', data=r_data)
    user_type = r.get_int('user_type', data=r_data, default=1)
    user_type = 0 if user_type == 0 else 1
    if not username or not password:
        return r.param_error(msg='用户名或密码不能为空')
    biz_user = BizUser()
    user_id = biz_user.insert_user(username=username, password=password, user_type=user_type, equipment=equipment,
                                   data_tagging=data_tagging, model_build=model_build, model_check=model_check)
    if user_id:
        return r.success(dict(user_id=user_id))
    else:
        return r.error()


@bp_page.route(f'/user/update', methods=g.SANIC_METHOD.post.value)
@auth()
@get_user([g.PERMISSIONS.teacher.value])
async def user_update(r: Handler):
    r_data = r.get_json()
    username = r.get_str('username', data=r_data)
    password = r.get_str('password', data=r_data)
    equipment = r.get_str('equipment', data=r_data)
    user_id = r.get_int('user_id', data=r_data)
    data_tagging = r.get_str('data_tagging', data=r_data)
    model_build = r.get_str('model_build', data=r_data)
    model_check = r.get_str('model_check', data=r_data)
    user_type = r.get_int('user_type', data=r_data, default=1)
    user_type = 0 if user_type == 0 else 1
    if not user_id or not username or not password:
        return r.param_error(msg='参数不能为空')
    biz_user = BizUser()
    update_status = biz_user.update_user(user_id=user_id, user_type=user_type, username=username, password=password,
                                         equipment=equipment, data_tagging=data_tagging, model_build=model_build,
                                         model_check=model_check)
    if update_status:
        return r.success(dict(user_id=user_id))
    else:
        return r.error("修改失败")


@bp_page.route(f'/user/delete', methods=g.SANIC_METHOD.post.value)
@auth()
@get_user([g.PERMISSIONS.teacher.value])
async def user_delete(r: Handler):
    r_data = r.get_json()
    user_id = r.get_int('user_id', data=r_data)
    if not user_id:
        return r.param_error(msg='user_id不能为空')
    biz_user = BizUser()
    update_status = biz_user.delete_user(user_id=user_id)
    if update_status:
        return r.success(dict())
    else:
        return r.error(msg="删除失败")

# @bp_page.route(f'/equipment/list', methods=g.SANIC_METHOD.get.value)
# @auth()
# @get_user([g.PERMISSIONS.teacher.value])
# async def equipment_list(r: Handler):
#     page = r.get_int('page', default=1)
#     limit = r.get_int('limit', default=10)
#     if page < 1:
#         page = 1
#     if limit < 1:
#         limit = 1
#     elif limit > 100:
#         limit = 100
#     data = BizUser().get_equipment_pagination(offset=(page - 1) * limit, limit=limit)
#
#     return r.success(dict(data=data))
#
#
# @bp_page.route(f'/equipment/insert', methods=g.SANIC_METHOD.post.value)
# @auth()
# @get_user([g.PERMISSIONS.teacher.value])
# async def equipment_insert(r: Handler):
#     r_data = r.get_json()
#     name = r.get_str('name', data=r_data)
#     ip = r.get_str('ip', data=r_data)
#     desc = r.get_str('desc', data=r_data)
#     if not name or not ip or not desc:
#         return r.param_error(msg='参数不能为空')
#     biz_user = BizUser()
#     equipment_id = biz_user.insert_equipment(name=name, ip=ip, desc=desc)
#     if equipment_id:
#         return r.success(dict(equipment_id=equipment_id))
#     else:
#         return r.error(msg='添加失败')
#
#
# @bp_page.route(f'/equipment/update', methods=g.SANIC_METHOD.post.value)
# @auth()
# @get_user([g.PERMISSIONS.teacher.value])
# async def equipment_update(r: Handler):
#     r_data = r.get_json()
#     name = r.get_str('name', data=r_data)
#     ip = r.get_str('ip', data=r_data)
#     desc = r.get_str('desc', data=r_data)
#     equipment_id = r.get_int('equipment_id', data=r_data)
#     if not name or not ip or not desc or not equipment_id:
#         return r.param_error(msg='参数不能为空')
#     biz_user = BizUser()
#     update_status = biz_user.update_equipment(equipment_id=equipment_id, name=name, ip=ip,
#                                               desc=desc)
#     if update_status:
#         return r.success(dict(equipment_id=equipment_id))
#     else:
#         return r.error("修改失败")
#
#
# @bp_page.route(f'/equipment/delete', methods=g.SANIC_METHOD.post.value)
# @auth()
# @get_user([g.PERMISSIONS.teacher.value])
# async def equipment_delete(r: Handler):
#     r_data = r.get_json()
#     equipment_id = r.get_int('equipment_id', data=r_data)
#     if not equipment_id:
#         r.param_error('equipment_id不能为空')
#     biz_user = BizUser()
#     update_status = biz_user.delete_equipment(equipment_id=equipment_id)
#     if update_status:
#         return r.success(dict())
#     else:
#         return r.error(msg="删除失败")
