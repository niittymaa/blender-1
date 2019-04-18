#pragma once

#include "FN_core.hpp"

namespace FN {
namespace Functions {

SharedFunction &GET_FN_bool_to_int32();
SharedFunction &GET_FN_bool_to_float();
SharedFunction &GET_FN_int32_to_float();
SharedFunction &GET_FN_int32_to_bool();
SharedFunction &GET_FN_float_to_int32();
SharedFunction &GET_FN_float_to_bool();

SharedFunction &GET_FN_bool_list_to_int32_list();
SharedFunction &GET_FN_bool_list_to_float_list();
SharedFunction &GET_FN_int32_list_to_float_list();
SharedFunction &GET_FN_int32_list_to_bool_list();
SharedFunction &GET_FN_float_list_to_int32_list();
SharedFunction &GET_FN_float_list_to_bool_list();

}  // namespace Functions
}  // namespace FN
