import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InstructorHomeComponent } from './home/Instructor-home.component';
import { InstructorNewComponent } from './new/Instructor-new.component';
import { InstructorDetailComponent } from './detail/Instructor-detail.component';

const routes: Routes = [
  {path: '', component: InstructorHomeComponent},
  { path: 'new', component: InstructorNewComponent },
  { path: ':id', component: InstructorDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Instructor-detail-permissions'
      }
    }
  },{
    path: ':instructor_id/Course', loadChildren: () => import('../Course/Course.module').then(m => m.CourseModule),
    data: {
        oPermission: {
            permissionId: 'Course-detail-permissions'
        }
    }
},{
    path: ':instructor_id/InstructorAssignment', loadChildren: () => import('../InstructorAssignment/InstructorAssignment.module').then(m => m.InstructorAssignmentModule),
    data: {
        oPermission: {
            permissionId: 'InstructorAssignment-detail-permissions'
        }
    }
}
];

export const INSTRUCTOR_MODULE_DECLARATIONS = [
    InstructorHomeComponent,
    InstructorNewComponent,
    InstructorDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class InstructorRoutingModule { }