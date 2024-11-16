import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CourseMaterialHomeComponent } from './home/CourseMaterial-home.component';
import { CourseMaterialNewComponent } from './new/CourseMaterial-new.component';
import { CourseMaterialDetailComponent } from './detail/CourseMaterial-detail.component';

const routes: Routes = [
  {path: '', component: CourseMaterialHomeComponent},
  { path: 'new', component: CourseMaterialNewComponent },
  { path: ':id', component: CourseMaterialDetailComponent,
    data: {
      oPermission: {
        permissionId: 'CourseMaterial-detail-permissions'
      }
    }
  }
];

export const COURSEMATERIAL_MODULE_DECLARATIONS = [
    CourseMaterialHomeComponent,
    CourseMaterialNewComponent,
    CourseMaterialDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CourseMaterialRoutingModule { }